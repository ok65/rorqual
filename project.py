
# Library import
import configg
import json


class Project:

    def __init__(self, path: str):
        self._data = configg.Configg(path, data_backend=configg.JSON_BACKEND)

    @classmethod
    def new(cls, path: str):
        with open("VERSION", "r") as fp:
            version = fp.readline().strip()

        setup_data = {"version": version,
                      "links": {},
                      "documents": {}
                      }

        with open(path, "x") as fp:
            json.dump(setup_data, fp)

        return Project(path)

    def new_document(self, title: str, stub: str):
        setup_data = {"title": title}