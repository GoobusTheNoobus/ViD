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
import sys
import file_handler
import key_input

from editor import Editor
from renderer import Renderer


def main(window: curses.window) -> None:

    file_path = sys.argv[1] if len(sys.argv) > 1 else ''

    editor = Editor()
    renderer = Renderer(window)

    editor.load(file_path)
    
    curses.start_color()

    while True:
        renderer.render(editor)

        key = window.getch()





        # navigation

        if key == key_input.ESC:
            return

        elif key == key_input.UP:
            editor.up()

        elif key == key_input.DOWN:
            editor.down()

        elif key == key_input.LEFT:
            editor.left()

        elif key == key_input.RIGHT:
            editor.right()

        elif key == key_input.ENTER:
            editor.insert_newline()

        elif key == key_input.BACKSPACE:
            editor.backspace()

        elif key == key_input.CTRL_O:
            editor.save()

        elif 32 <= key <= 126:
            editor.insert(chr(key))


if __name__ == "__main__":
    # we run some setups
    curses.set_escdelay(25)
    
    curses.wrapper(main)
