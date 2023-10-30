
# Library imports
import json


class JsonDataClass:

    def __init__(self, json_path: str):
        self.data = {}
        self._file_path = json_path
        self.load()

    def load(self):
        with open(self._file_path, "r") as fp:
            self.data = json.load(fp)

    def save(self):
        with open(self._file_path, "w+") as fp:
            json.dump(self.data, fp)

    def lock(self):
        pass


if __name__ == "__main__":

    pass