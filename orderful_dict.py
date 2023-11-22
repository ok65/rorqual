# Library imports
from typing import Any, Tuple, List, Dict


class OrderfulDict:

    def __init__(self):
        self._map = {}
        self._order = []
        self._iter_idx = 0

    def __len__(self) -> int:
        return len(self._order)

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx >= len(self._order):
            raise StopIteration
        x = self._map[self._order[self._iter_idx]]
        self._iter_idx += 1
        return x

    def __contains__(self, key):
        return key in self._order

    def set(self, key: Any, value: Any, index: int = -1):
        self._map[key] = value
        if key in self._order:
            self._order.remove(key)
        index = len(self._order) if index < 0 else index
        self._order.insert(index, key)

    def get_idx(self, index) -> Any:
        return self._map[self._order[index]]

    def get_key(self, key) -> Any:
        return self._map[key]

    def move_key(self, key, new_index):
        self._order.remove(key)
        new_index = len(self._order) if new_index < 0 else new_index
        self._order.insert(new_index, key)

    def pack(self) -> Dict:
        return {"__OrderfulDict__": {"order": self._order, "map": self._map}}

    def get_list(self):
        return [self._map[x] for x in self._order]

    @classmethod
    def unpack(cls, pack) -> 'OrderfulDict':
        od = cls()
        od._map = pack["__OrderfulDict__"]["map"]
        od._order = pack["__OrderfulDict__"]["order"]
        return od
