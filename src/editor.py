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

import file_handler


class Editor:
    """

    :var lines: the text displayed, split by new-lines
    :var cursor_x: column index of the cursor
    :var cursor_y: line index of the cursor
    :var file_path: the path to the file the editor is emulating
    """

    def __init__(self) -> None:
        self.lines = ['']
        self.file_path = ''
        self.cursor_x = 0
        self.cursor_y = 0

    def load(self, file_path : str) -> None:

        text = file_handler.read(file_path)

        if not text:
            return

        self.file_path = file_path
        self.lines = text.split("\n")

    def save(self) -> None:

        text = ''
        for i, line in enumerate(self.lines):
            text += line
            if i != len(self.lines) - 1:
                text += '\n'

        success = file_handler.write(self.file_path, text)

        if not success:
            pass # TODO: raise error menu

    def insert(self, char: str):
        assert len(char) == 1

        line = self.lines[self.cursor_y]

        self.lines[self.cursor_y] = line[:self.cursor_x] + char + line[self.cursor_x:]

        self.cursor_x += 1

    def insert_newline(self):

        line = self.lines[self.cursor_y]

        before_cursor = line[:self.cursor_x]
        after_cursor = line[self.cursor_x:]

        self.lines[self.cursor_y] = before_cursor
        self.lines.insert(self.cursor_y + 1, after_cursor)

        self.cursor_y += 1
        self.cursor_x = 0

    def backspace(self):

        if self.cursor_x > 0:
            line = self.lines[self.cursor_y]

            self.lines[self.cursor_y] = line[:self.cursor_x - 1] + line[self.cursor_x:]

            self.cursor_x -= 1

        elif self.cursor_y > 0:
            previous_line = self.lines[self.cursor_y - 1]
            current_line = self.lines[self.cursor_y]

            self.cursor_x = len(previous_line)

            self.lines[self.cursor_y - 1] = previous_line + current_line
            self.lines.pop(self.cursor_y)

            self.cursor_y -= 1

    def up(self) -> None:
        self.cursor_y = max(0, self.cursor_y - 1)

        # if the current line is longer than the destination and the cursor would move into non-existent
        # space, we must cap the cursor's x coord
        self.cursor_x = min(self.cursor_x, len(self.lines[self.cursor_y]))

    def down(self) -> None:
        height = len(self.lines) - 1
        self.cursor_y = min(height, self.cursor_y + 1)

        # if the current line is longer than the destination and the cursor would move into non-existent
        # space, we must cap the cursor's x coord
        self.cursor_x = min(self.cursor_x, len(self.lines[self.cursor_y]))

    def left(self) -> None:
        self.cursor_x = max(0, self.cursor_x - 1)

    def right(self) -> None:
        width = len(self.lines[self.cursor_y]) # calculate the width of the current line
        self.cursor_x = min(width, self.cursor_x + 1)