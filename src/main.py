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
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Missing input file! Usage: vid <filename>")
        sys.exit(1)

if __name__ == "__main__":
    main()
