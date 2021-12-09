def read_input(file_path):
    import os
    from pathlib import Path
    with open(os.path.join(Path(file_path).parent, "input.txt")) as fp:
        input_ = fp.read().splitlines()
    return input_