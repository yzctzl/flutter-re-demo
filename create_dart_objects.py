import sys, os
import idaapi, ida_kernwin
try:
    import flure
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

idaapi.require("flure.ida.dart_obj_create")
from flure.ida.dart_obj_create import DartObjectsCreator


if __name__ == "__main__":
    object_pool_address = ida_kernwin.ask_addr(0xbc980021 - 1, "Please enter Object Pool address")
    if object_pool_address is not None:
        dart_object_creator = DartObjectsCreator(object_pool_address)
        dart_object_creator.create_all_objects()
