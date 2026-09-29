

def write_to_file(file_path : str) -> void: # Please only pass raw strings to this function
    pass

def get_all_file_contents(file_path : str) -> str: # Please only pass raw strings to this function
    with open("demofile.txt") as f:
        print(f.read())