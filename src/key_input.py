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

import curses

def _ctrl_code(char: str) -> int:
    assert len(char) == 1
    return ord(char.upper()) - ord('@')

def decode_key(key: int) -> str | None:

    if 0 <= key <= 255:
        return chr(key) # normal character keys
    return None

CTRL_Q = _ctrl_code('q')
CTRL_C = _ctrl_code('c')
CTRL_V = _ctrl_code('v')
CTRL_T = _ctrl_code('t')

ESC = 27

LEFT = curses.KEY_LEFT
RIGHT = curses.KEY_RIGHT
UP = curses.KEY_UP
DOWN = curses.KEY_DOWN
