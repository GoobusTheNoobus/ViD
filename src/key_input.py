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
    """Gets the curses key id of the ctrl+sequence

    :param char: the keypress alongside ctrl
    :return: the id of the sequence
    """

    assert len(char) == 1
    return ord(char.upper()) - ord('@')

CTRL_Q = _ctrl_code('q')
CTRL_C = _ctrl_code('c')
CTRL_V = _ctrl_code('v')
CTRL_T = _ctrl_code('t')
CTRL_O = _ctrl_code('o')

ESC = 27

LEFT  = curses.KEY_LEFT
RIGHT = curses.KEY_RIGHT
UP    = curses.KEY_UP
DOWN  = curses.KEY_DOWN

BACKSPACE       = 127
ENTER           = 10
