from objc_util import load_framework, ObjCClass
for fw in ('Metal', 'MetalKit', 'QuartzCore'):
    load_framework(fw)
class_names = [
    'CAMetalLayer',
    'MTKView',
    'MTLDevice',
    'MTLCommandQueue',
    'MTLCommandBuffer',
    'MTLRenderCommandEncoder',
    'MTLComputeCommandEncoder',
    'MTLBlitCommandEncoder',
    'MTLParallelRenderCommandEncoder',
    'MTLTileRenderCommandEncoder',
    'MTLRenderPassDescriptor',
    'MTLRenderPassColorAttachmentDescriptor',
    'MTLRenderPassDepthAttachmentDescriptor',
    'MTLRenderPassStencilAttachmentDescriptor',
    'MTLRenderPipelineDescriptor',
    'MTLRenderPipelineState',
    'MTLRenderPipelineColorAttachmentDescriptor',
    'MTLRenderPipelineFunctionsDescriptor',
    'MTLComputePipelineDescriptor',
    'MTLComputePipelineState',
    'MTLFunction',
    'MTLLibrary',
    'MTLBuffer',
    'MTLTextureDescriptor',
    'MTLTexture',
    'MTKTextureLoader',
    'MTLDepthStencilDescriptor',
    'MTLDepthStencilState',
    'MTLVertexDescriptor',
    'MTLVertexAttributeDescriptor',
    'MTLVertexBufferLayoutDescriptor',
    'MTLSamplerDescriptor',
    'MTLSamplerState',
    'MTLArgumentEncoder',
    'MTLArgument',
    'MTLIndirectCommandBuffer',
    'MTLIndirectCommandBufferDescriptor',
    'MTLIntersectionFunctionTableDescriptor',
    'MTLIntersectionFunctionTable',
    'MTLAccelerationStructureDescriptor',
    'MTLAccelerationStructureGeometryDescriptor',
    'MTLAccelerationStructureBoundingBoxGeometryDescriptor',
    'MTLAccelerationStructureCurveGeometryDescriptor',
    'MTLAccelerationStructureTriangleGeometryDescriptor',
    'MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor',
    'MTLAccelerationStructureMotionCurveGeometryDescriptor',
    'MTLAccelerationStructurePassDescriptor',
    'MTLHeap',
    'MTLHeapDescriptor',
    'MTLFence',
]
available = []
missing = []

for name in class_names:
    try:
        ObjCClass(name)
        available.append(name)
    except (NameError, Exception):
        missing.append(name)
print('✅ Available classes (%d):\n%s\n' % (len(available), ', '.join(available)))
print('❌ Missing classes (%d):\n%s'  % (len(missing),  ', '.join(missing)))
