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
import colour

from editor import Editor
from misc import *

class Renderer:
    """

    :var window: a stored reference to the running window
    :var theme: the used theme
    """

    def __init__(self, window : curses.window):
        self.window = window
        self.theme = {
            'background': colour.BLACK,
            'foreground': colour.WHITE,

            'line_number': colour.GREEN,
            'selected_line_number': colour.WHITE,

            'status_bg': colour.DARK_GRAY,
            'status_fg': colour.WHITE,
            'status_vid_bg': colour.MAGENTA,
        }

        try:
            curses.curs_set(1)
        except curses.error:
            pass

        # initialize the colour schemes
        curses.init_pair(1, self.theme['foreground'], self.theme['background'])
        curses.init_pair(2, self.theme['line_number'], self.theme['background'])
        curses.init_pair(3, self.theme['selected_line_number'], self.theme['background'])

        curses.init_pair(4, self.theme['status_fg'], self.theme['status_bg'])
        curses.init_pair(5, self.theme['status_fg'], self.theme['status_vid_bg'])

    def render(self, editor : Editor):
        self.window.erase()

        height, width = self.window.getmaxyx()

        # reserve the last row for status bar
        editor_height = height - 1

        num_length = len(str(len(editor.lines)))
        self.window.bkgd(' ', curses.color_pair(1))
        
        for y, line in enumerate(editor.lines):
            if y == editor_height:
                break

            line_num = str(y + 1)
            extra_spaces = ' ' * (num_length - len(line_num))

            self.window.addstr(y, 0, ' ' + extra_spaces + line_num + ' ', 
                curses.color_pair(
                    2 if y != editor.cursor_y else 3) | curses.A_BOLD) # if the current line is selected, show different colour

            self.window.addstr(y, 2 + len(line_num) + len(extra_spaces), line, curses.color_pair(1))

        vid_text = f" VID {VERSION}  "
        vid_text_len = len(vid_text)

        self.window.addstr(editor_height, 0, vid_text, curses.color_pair(5) | curses.A_BOLD)
        self.window.addstr(editor_height, vid_text_len, '  ' + editor.file_path + ' ' * (width - vid_text_len -
            len(editor.file_path) - 3), curses.color_pair(4))

        self.window.move(editor.cursor_y, editor.cursor_x + 2 + num_length)
            
        self.window.refresh()

    def clearscreen(self):
        self.window.erase()
        self.window.refresh()
    
    def render_text(self, text : str) -> None:
        self.window.addstr(text)
