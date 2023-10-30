
# Library imports
from typing import TYPE_CHECKING, Dict
import json

# Project imports
from json_data_class import JsonDataClass
if TYPE_CHECKING:
    from project import Project


class Document(JsonDataClass):

    def __init__(self, project: 'Project', stub: str):
        self._project = project
        super().__init__(f"{self._project.path}//{stub}.json")
        self.data = {}
        self.load()

    @classmethod
    def new(cls, path, title, stub):
        setup_data = {"header": {"title": title, "stub": stub, "next_id": 1}, "content": []}
        with open(path, "x") as fp:
            json.dump(setup_data, fp)

    def load(self):
        with open(self._file_path, "r") as fp:
            self.data = json.load(fp)

    def save(self):
        with open(self._file_path, "w+") as fp:
            json.dump(self.data, fp)

    def add_item(self, content: Dict, ):
        pass

    def insert_content(self, index: int, text_context: str):
        self.data["content"].insert(index, {"id": self._get_next_id(), "content": text_context})

    def _get_next_id(self) -> int:
        id = self.data["header"]["next_id"]
        self.data["header"]["next_id"] += 1
        return id