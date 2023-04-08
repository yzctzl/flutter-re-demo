import sys, os
import idaapi, ida_kernwin, ida_segment

try:
    import flure
except ImportError:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

idaapi.require("flure.ida.create_segment")
from flure.ida.create_segment import add_dartvm_segment

dump_files = [""]

if __name__ == "__main__":
    for dump_file in dump_files:
        rw_memory_file_name = ida_kernwin.ask_file(False,
                                                f"~/Desktop/shenhu/dump/{dump_file}",
                                                "Flutter RW memory filename")
        if rw_memory_file_name is not None:
            try:
                guessed_rw_memory_address = int(os.path.basename(rw_memory_file_name), 16)
            except ValueError:
                guessed_rw_memory_address = 0
            rw_memory_address = ida_kernwin.ask_addr(guessed_rw_memory_address, "Please enter Flutter RW memory address")
            if rw_memory_address is not None:
                print(f"Mapping {rw_memory_file_name} at 0x{rw_memory_address:x}")
                add_dartvm_segment(rw_memory_address, f"dump_{dump_file}", ida_segment.SEGPERM_WRITE | ida_segment.SEGPERM_READ,
                                rw_memory_file_name)


