
# Library imports
from typing import TYPE_CHECKING, Dict, List
import json

# Project imports
from json_data_class import JsonDataClass, autosave_json, new_jdc_file
from linkage import Linkage
from artefact import Artefact
from orderful_dict import OrderfulDict
if TYPE_CHECKING:
    from project import Project


class Document(JsonDataClass):

    def __init__(self, project: 'Project', uid: str):
        self._project = project
        super().__init__(uid, f"{self._project.path}//{uid}.json")

    @property
    def title(self) -> str:
        return self.data["title"]

    @title.setter
    @autosave_json
    def title(self, new_title: str):
        self.data["title"] = new_title

    @classmethod
    def new(cls, project: 'Project', path: str, uid: str, title: str) -> 'Document':
        new_jdc_file(uid=uid, json_path=path, data_dict={"uid": uid, "title": title, "next_art_uid": 1,
                                                         "content": OrderfulDict(), "linkage": {}})
        return cls(project=project, uid=uid)

    @autosave_json
    def new_artefact(self, content: str, index: int = -1) -> Artefact:
        index = index if index >= 0 else len(self.data["content"])
        return Artefact.new(self, uid=self.new_uid(), content=content, index=index)

    @autosave_json
    def move_artefact(self, uid: str, new_index: int) -> None:
        self.data["content"].move_key(uid, new_index)

    def get_local_artefact(self, uid) -> Artefact:
        if uid not in self.data["content"]:
            raise IndexError(f"UID ({uid}) not found in document ({self.uid})")
        return Artefact(uid=uid, document=self)

    def get_local_artefact_links(self, destination_art_uid: str) -> List[Linkage]:
        d = self.data["linkage"]

        return [self.get_local_link(link["uid"]) for link in self.data["linkage"].values() if
                link["destination"]["artefact"]["uid"] == destination_art_uid]

    def get_local_link(self, uid) -> Linkage:
        return Linkage(document=self, uid=uid)

    @autosave_json
    def new_linkage(self, source_artefact: Artefact, destination_doc_uid: str, destination_art_uid: str, link_type: str)\
            -> Linkage:
        return Linkage.new(uid=self.new_uid(), source_artefact=source_artefact, link_type=link_type,
                           destination_doc_uid=destination_doc_uid, destination_art_uid=destination_art_uid)

    def new_uid(self) -> str:
        uid = self.data["next_art_uid"]
        self.data["next_art_uid"] += 1
        return str(uid)

    def get_local_artefact_list(self) -> List:
        return [self.get_local_artefact(d["uid"]) for d in self.data["content"].get_list()]

