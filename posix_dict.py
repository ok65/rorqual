
# Library imports
from pathlib import PurePosixPath


class PosixDict():

    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        pointer = self._data
        for path_chunk in PurePosixPath(key).parts:
            pointer = pointer[path_chunk]
        return pointer

    def __setitem__(self, key, value):
        pointer = self._data
        path_parts = PurePosixPath(key).parts[:-1]
        final_path_part = PurePosixPath(key).parts[-1:][0]
        for path_chunk in path_parts:
            if not isinstance(pointer.get(path_chunk), dict):
                pointer[path_chunk] = {}
            pointer = pointer[path_chunk]
        pointer[final_path_part] = value

    def load(self, data: dict):
        self._data = data

    def cut(self, key) -> 'PosixDict':
        pd = PosixDict()
        pd.load(self[key])
        return pd

    def dump(self) -> dict:
        return self._data

