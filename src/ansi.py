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

RESET = '\033[0m'

# text decorations
BOLD = '\033[1m'

# foreground colours
FG_RED         = '\033[31m'
FG_GREEN       = '\033[32m'
FG_YELLOW      = '\033[33m'
FG_BLUE        = '\033[34m'
FG_MAGENTA     = '\033[35m'
FG_CYAN        = '\033[36m'

# background colours
BG_RED         = '\033[41m'
BG_GREEN       = '\033[42m'
BG_YELLOW      = '\033[43m'
BG_BLUE        = '\033[44m'
BG_MAGENTA     = '\033[45m'
BG_CYAN        = '\033[46m'

def clear_terminal() -> None:
    print('\033[2J\033[H\0333', end='')



