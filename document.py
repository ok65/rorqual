
# Library imports
from typing import TYPE_CHECKING, Dict, List
import json

# Project imports
from json_data_class import JsonDataClass, autosave_json
from artefact import Artefact
if TYPE_CHECKING:
    from project import Project


class Document(JsonDataClass):

    def __init__(self, project: 'Project', uid: str):
        self._project = project
        super().__init__(uid, f"{self._project.path}//{uid}.json")

    @property
    def title(self):
        return self.data["title"]

    @title.setter
    @autosave_json
    def title(self, new_title: str):
        self.data["title"] = new_title

    @classmethod
    def new(cls, project: 'Project', path: str, uid: str, title: str) -> 'Document':
        setup_data = {"uid": uid, "title": title, "next_art_uid": 1, "content": [], "links": []}
        with open(path, "x") as fp:
            json.dump(setup_data, fp)
        return cls(project=project, uid=uid)

    @autosave_json
    def new_artefact(self, content: str, index: int = -1) -> Artefact:
        index = index if index >= 0 else len(self.data["content"])
        return Artefact.new(self, uid=self.new_uid(), content=content, index=index)

    def get_local_artefact(self, uid):
        a = [art for art in self.data["content"] if art.get("uid") == uid][0]
        return Artefact(uid=uid, document=self, )

    @autosave_json
    def new_linkage(self, source_artefact: Artefact, destination_doc_id: str, destination_art_id: str, link_type: str):
        pass

    def new_uid(self) -> str:
        uid = self.data["next_art_uid"]
        self.data["next_art_uid"] += 1
        return str(uid)

    def get_artefact_list(self) -> List:
        artefacts = []
        for d in self.data["content"]:
            artefacts.append(self.get_local_artefact(d["uid"]))
        return artefacts
