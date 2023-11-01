
# Library import
import json
import os
import uuid

# Project imports
from json_data_class import JsonDataClass
from document import Document


class Project(JsonDataClass):

    def __init__(self, path: str):
        super().__init__(path)
        self.path = os.path.split(path)[0]

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

    def new_document(self, title: str, stub: str) -> Document:
        setup_data = {"title": title, "stub": stub}
        if stub in self.data["documents"].keys():
            raise Exception("Stub not unique")
        self.data["documents"][stub] = setup_data

        with open(f"{self.path}//{stub}.json", "x") as fp:
            json.dump(setup_data, fp)

        return self.open_document(stub)

    def open_document(self, stub: str) -> Document:
        return Document(self, stub)


    def new_uid(self) -> str:
        return uuid.uuid4().hex