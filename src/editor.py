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

class Editor:
    def __init__(self) -> None:
        self.lines = [""]
        self.cursor_x = 0
        self.cursor_y = 0

    def load(self, text: str | None) -> None:
        if not text:
            return

        self.lines = text.split("\n")

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