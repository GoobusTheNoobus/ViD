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

        num_length = len(str(len(editor.lines)))
        
        for y, line in enumerate(editor.lines):
            line_num = str(y + 1)
            extra_spaces = ' ' * (num_length - len(line_num))
            
            self.window.addstr(y, 0, ' ' + extra_spaces + line_num + '  ' + line)

        self.window.move(editor.cursor_y, editor.cursor_x + 3 + num_length)
        self.window.refresh()