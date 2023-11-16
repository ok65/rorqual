
# Library imports
import json
import functools

# Project imports
from base import Base


class JsonDataClass(Base):

    def __init__(self, uid: str, json_path: str):
        super().__init__(uid)
        self.data = {}
        self._file_path = json_path
        self.load()

    def load(self):
        with open(self._file_path, "r") as fp:
            self.data = json.load(fp)

    def save(self):
        with open(self._file_path, "w+") as fp:
            json.dump(self.data, fp, sort_keys=False, indent=4)

    def lock(self):
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