
# Library imports
from pathlib import PurePosixPath
from typing import Dict, Optional


class PosixDict:

    def __init__(self, data_dict: Optional[Dict] = None):
        self._data = data_dict if data_dict else {}

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

    def values(self):
        return self._data.values()

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def load(self, data: dict):
        self._data = data

    def cut(self, key) -> 'PosixDict':
        pd = PosixDict()
        pd.load(self[key])
        return pd

    def dump(self) -> dict:
        return self._data

    def pack(self):
        return {"__PosixDict__": self._data}

    @staticmethod
    def unpack(packed: dict) -> 'PosixDict':
        return PosixDict(data_dict=packed["__PosixDict__"])

