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

def main() -> None:

    if len(sys.argv) == 1:
        print("Missing input file! Usage: vid <filename>")
        sys.exit(1)

    if (len(sys.argv) >= 3):
        print("Too many arguments! Usage: vid <filename>")

    file_path = sys.argv[1]

if __name__ == "__main__":
    main()
