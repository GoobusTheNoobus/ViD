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

# The renderer is the module that will perform all rendering.

import curses
from typing import overload


from editor import Editor

class Renderer:
    def __init__(self, window : curses.window):
        self.window = window
        self.theme = {
            'background': curses.COLOR_BLACK,
            'foreground': curses.COLOR_WHITE,
            'line_number': curses.COLOR_GREEN
        }

        curses.init_pair(1, self.theme['foreground'], self.theme['background'])
        curses.init_pair(2, self.theme['line_number'], self.theme['background'])

    def render(self, editor : Editor):
        self.window.erase()

        num_length = len(str(len(editor.lines)))
        self.window.bkgd(' ', curses.color_pair(1))
        
        for y, line in enumerate(editor.lines):
            line_num = str(y + 1)
            extra_spaces = ' ' * (num_length - len(line_num))

            self.window.addstr(y, 0, ' ' + extra_spaces + line_num + ' ', curses.color_pair(2))

            self.window.addstr(y, 2 + len(line_num) + len(extra_spaces), line, curses.color_pair(1))

        self.window.move(editor.cursor_y, editor.cursor_x + 2 + num_length)
        self.window.refresh()
    
    def clearscreen(self):
        self.window.erase()
        self.window.refresh()
    
    @overload
    def render(self, text : str) -> void:
        self.window.addstr(text)