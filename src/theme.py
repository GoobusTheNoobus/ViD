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

import colour

class Theme:
    """

    :var name: the name of the theme
    :var primary_bg: the main background colour of the editor
    :var secondary_bg: the secondary background colour of the editor (status bar background)
    :var special_bg: the background of the nameplate displaying 'VID {Version}'
    :var primary_fg: the main text colour of the editor
    :var secondary_fg: the secondary text colour of the editor (unselected line number and comments)
    """

    def __init__(self, name : str, primary_bg : int, secondary_bg : int, special_bg : int, primary_fg : int,
                 secondary_fg : int):
        self.name = name

        self.primary_bg = primary_bg
        self.secondary_bg = secondary_bg
        self.special_bg = special_bg
        self.primary_fg = primary_fg
        self.secondary_fg = secondary_fg


themes = [
    Theme('VID Dark (Default)', 234, 243, 208, 250, 242)
]
