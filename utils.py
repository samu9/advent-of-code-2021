from typing import List, Tuple, Union


def read_input(file_path):
    import os
    from pathlib import Path
    with open(os.path.join(Path(file_path).parent, "input.txt")) as fp:
        input_ = fp.read().splitlines()
    return input_


def clamp(value: int, range_: Union[List[int], Tuple[int]]):
    return min(max(range_[0], value), range_[1])