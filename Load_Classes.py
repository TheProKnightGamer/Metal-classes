from objc_util import load_framework, ObjCClass, ObjCInstance, c
from ctypes import c_void_p, c_int, c_char_p, POINTER
for fw in ('Metal', 'MetalKit', 'QuartzCore'):
    load_framework(fw)
c.objc_getClassList.restype  = c_int
c.objc_getClassList.argtypes = [POINTER(c_void_p), c_int]
c.class_getName.restype       = c_char_p
c.class_getName.argtypes      = [c_void_p]
n_classes = c.objc_getClassList(None, 0)
buffer   = (c_void_p * n_classes)()
c.objc_getClassList(buffer, n_classes)
wanted_prefixes = ('MTL', 'MTK')
wanted_exact    = ('CAMetalLayer',)
_found = {}
for ptr in buffer:
    name_ptr = c.class_getName(ptr)
    if not name_ptr:
        continue
    name = name_ptr.decode('utf-8')
    if name.startswith(wanted_prefixes) or name in wanted_exact:
        try:
            _found[name] = ObjCClass(name)
        except ValueError:
            pass
globals().update(_found)
c.MTLCreateSystemDefaultDevice.restype = c_void_p
def get_default_device():
    ptr = c.MTLCreateSystemDefaultDevice()
    return ObjCInstance(ptr)
defaultDevice = get_default_device()
if __name__ == '__main__':
    print(f"Found {len(_found)} Metal/MetalKit/CoreAnimation classes:")
    for nm in sorted(_found):
        print(nm)
    print('\nDefault device →', defaultDevice)
    print('name:', defaultDevice.name())
    if 'MTKView' in _found:
        v = MTKView.alloc().init()
        print('MTKView instance →', v)
globals().update(_found)
__all__ = list(_found.keys())
def test_imports():
    import importlib
    this_mod = importlib.import_module(__name__)
    successes, failures = [], []
    for cls_name in __all__:
        try:
            getattr(this_mod, cls_name)
        except AttributeError:
            failures.append(cls_name)
        else:
            successes.append(cls_name)
    print(f"✅ Imported {len(successes)} classes")
    if failures:
        print(f"❌ Failed to import {len(failures)} classes: {failures}")
c.MTLCreateSystemDefaultDevice.restype = c_void_p
def get_default_device():
    ptr = c.MTLCreateSystemDefaultDevice()
    return ObjCInstance(ptr)

defaultDevice = get_default_device()

if __name__ == '__main__':
    print(f"Found {len(_found)} Metal/MetalKit/CoreAnimation classes:")
    for nm in sorted(_found):
        print(nm)
    print('\nDefault device →', defaultDevice)
    print('name:', defaultDevice.name())
    if 'MTKView' in _found:
        v = MTKView.alloc().init()
        print('MTKView instance →', v)
    print('\nTesting importability of each class...')
    test_imports()
