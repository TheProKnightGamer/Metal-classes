from ctypes import c_void_p, c_int, POINTER, CDLL
from objc_util import load_framework, ObjCClass, c, ObjCInstance

for fw in ('Metal', 'MetalKit', 'QuartzCore'):
    load_framework(fw)

metal = CDLL('/System/Library/Frameworks/Metal.framework/Metal')
metal.MTLCreateSystemDefaultDevice.restype = c_void_p
metal.MTLCreateSystemDefaultDevice.argtypes = []

total = c.objc_getClassList(None, 0)
buffer = (c_void_p * total)()
c.objc_getClassList(buffer, total)

def _import_mtl_proto(proto_name):
    suffix = proto_name[3:]
    for ptr in buffer:
        name = c.class_getName(ptr).decode('utf-8')
        if name.startswith('MTL') and name.endswith(suffix):
            try:
                return ObjCClass(name)
            except NameError:          
                continue
    raise ImportError(f"No concrete class found for {proto_name!r}")
_protocols = [
    'MTLDevice', 'MTLCommandQueue', 'MTLCommandBuffer',
    'MTLRenderCommandEncoder', 'MTLComputeCommandEncoder', 'MTLBlitCommandEncoder',
    'MTLParallelRenderCommandEncoder',
    'MTLRenderPipelineState', 'MTLComputePipelineState', 'MTLFunction',
    'MTLLibrary', 'MTLBuffer', 'MTLTexture', 'MTLDepthStencilState',
    'MTLSamplerState', 'MTLArgumentEncoder', 'MTLIndirectCommandBuffer',
    'MTLIntersectionFunctionTable', 'MTLHeap', 'MTLFence',
]
for proto in _protocols:
    try:
        cls = _import_mtl_proto(proto)
        globals()[proto] = cls
    except ImportError as e:
        globals()[proto] = None
        print(f"⚠️  Warning: {e}")

#if __name__ == '__main__':
#    for proto in _protocols:
#        print(f"{proto}: {globals()[proto]}")
MTLCreateSystemDefaultDevice = metal.MTLCreateSystemDefaultDevice
