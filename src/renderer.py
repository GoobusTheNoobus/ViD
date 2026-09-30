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

from editor import Editor

class Renderer:
    def __init__(self, window : curses.window):
        self.window = window

    def render(self, editor : Editor):
        self.window.erase()

        for y, line in enumerate(editor.lines):
            self.window.addstr(y, 0, line)

        self.window.move(editor.cursor_y, editor.cursor_x)
        self.window.refresh()