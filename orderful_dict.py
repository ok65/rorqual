# Library imports
from typing import Any, Tuple, List, Dict


class OrderfulDict:

    def __init__(self):
        self._mapping = {}
        self._order = []

    def __len__(self) -> int:
        return len(self._order)

    def set(self, key: Any, value: Any, index: int = -1):
        self._mapping[key] = value
        if key in self._order:
            self._order.remove(key)
        index = len(self._order) if index < 0 else index
        self._order.insert(index, key)

    def get_idx(self, index) -> Any:
        return self._mapping[self._order[index]]

    def get_key(self, key) -> Any:
        return self._mapping[key]

    def move_key(self, key, new_index):
        self._order.remove(key)
        new_index = len(self._order) if new_index < 0 else new_index
        self._order.insert(new_index, key)

    def pack(self) -> Dict:
        return {"__OrderfulDict__": {"order": self._order, "map": self._mapping}}

    @classmethod
    def unpack(cls, pack) -> 'OrderfulDict':
        od = cls()
        od._mapping = pack["__OrderfulDict__"]["map"]
        od._order = pack["__OrderfulDict__"]["order"]
        return od
