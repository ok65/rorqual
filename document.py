
# Library imports
from typing import TYPE_CHECKING, Dict, List
import json

# Project imports
from json_data_class import JsonDataClass
from artefact import Artefact
if TYPE_CHECKING:
    from project import Project


class Document(JsonDataClass):

    def __init__(self, project: 'Project', stub: str):
        self._project = project
        super().__init__(f"{self._project.path}//{stub}.json")

    @classmethod
    def new(cls, path, title, stub):
        setup_data = {"header": {"title": title, "stub": stub, "next_id": 1, "list_of_ids": []}, "content": []}
        with open(path, "x") as fp:
            json.dump(setup_data, fp)

    def add_item(self, content: Dict, ):
        pass

    def new_artefact(self, text_content: str, index: int = -1):
        _id =  self._get_next_id()
        index = index if index >= 0 else len(self.data["header"]["list_of_ids"])
        self.data["content"].insert(index, {"id": _id, "content": text_content})
        self.data["header"]["list_of_ids"].append(_id)
        return self.get(_id)

    def get(self, id):
        if id in self.data["header"]["list_of_ids"]:
            return Artefact(self, id)

    def _get_next_id(self) -> int:
        _id = self.data["header"]["next_id"]
        self.data["header"]["next_id"] += 1
        return _id

    def get_artefact_list(self) -> List:
        artefacts = []
        for d in self.data["content"]:
            artefacts.append(self.get(d["id"]))
        return artefacts
