
# Library imports
import json
import functools

# Project imports
from base import Base
from posix_dict import PosixDict
from orderful_dict import OrderfulDict


def new_jdc_file(uid: str, json_path: str, data_dict: dict) -> 'JsonDataClass':
    with open(json_path, "x") as fp:
        json.dump(data_dict, fp, sort_keys=False, indent=4, default=JsonDataClass._default_pack)
    return JsonDataClass(uid=uid, json_path=json_path)


class JsonDataClass(Base):

    def __init__(self, uid: str, json_path: str):
        super().__init__(uid)
        self.data = PosixDict()
        self._file_path = json_path
        self.load()

    def load(self):
        with open(self._file_path, "r") as fp:
            self.data.load(json.load(fp, object_hook=self._default_unpack))

    def save(self):
        with open(self._file_path, "w+") as fp:
            json.dump(self.data.dump(), fp, sort_keys=False, indent=4, default=self._default_pack)

    @staticmethod
    def _default_pack(data):
        return data.pack()

    @staticmethod
    def _default_unpack(data):
        if isinstance(data, dict):
            if "__OrderfulDict__" in data:
                return OrderfulDict.unpack(data)
            elif "__PosixDict__" in data:
                return PosixDict.unpack(data)
        return data

    def lock(self):
        pass


def myhook(data):
    d = data
    pass

def autosave_json(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        ret = f(*args, **kwargs)
        args[0].save()
        return ret
    return wrapper




if __name__ == "__main__":

    pass