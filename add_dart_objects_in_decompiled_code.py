import sys, os
import idaapi, ida_kernwin

try:
    import flure
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

idaapi.require("flure.ida.object_pool_microcode")
from flure.ida.object_pool_microcode import R5ReplaceHook

if __name__ == "__main__":
    try:
        r5_replace_hook.unhook()
        del r5_replace_hook
    except NameError as e:
        pass
    finally:
        object_pool_address = ida_kernwin.ask_addr(0xbc980021 - 1, "Please enter Object Pool address")
        if object_pool_address is not None:
            flure.ida.object_pool_microcode.OBJECT_POOL_PTR = object_pool_address
            r5_replace_hook = R5ReplaceHook()  # 将原来的 r5 + xxx 替换为 Object pool 中的 object
            r5_replace_hook.hook()
            print("Microcode R5 hook registered")
