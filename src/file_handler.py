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

def write(file_path : str, contents : str) -> bool:
    """Writes text to a file

    :param file_path: path to the file
    :param contents: what to write
    :return whether the write was successful
    """

    try:
        with open(file_path, 'w') as f:
            f.write(contents)
            return True
    except OSError:
        return False



def read(file_path : str) -> str | None:
    """Reads text from a file

    :param file_path: path to the file
    :return: the text if read is successful, otherwise None
    """
    try:
        with open(file_path) as f:
            return f.read()
    except OSError:
        return None

