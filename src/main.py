# =====================================================================
#
#                        __     ___ ____
#                        \ \   / (_)  _ \
#                         \ \ / /| | | | |
#                          \ V / | | |_| |
#                           \_/  |_|____/
#
#
# =====================================================================
#
# ViD is licensed under the MIT License. All rights reserved.

import ansi
import sys
import file_handler

def main() -> None:

    if len(sys.argv) == 1:
        print("ERROR: Missing input file! \nUsage: vid <filename>")
        sys.exit(1)

    if (len(sys.argv) >= 3):
        print("ERROR: Too many arguments! \nUsage: vid <filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    print(file_handler.read(file_path))

if __name__ == "__main__":
    main()
