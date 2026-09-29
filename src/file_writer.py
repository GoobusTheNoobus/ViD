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


def write_to_file(file_path : str, contents : str) -> void: # Please only pass raw strings to this function
    with open(file_path, 'w') as f:
        f.write(contents)


def get_all_file_contents(file_path : str) -> str: # Please only pass raw strings to this function
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File '" + file_path + "' was not found.")