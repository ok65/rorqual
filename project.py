
# Library import
import json
import os
import uuid
from typing import List

# Project imports
from json_data_class import JsonDataClass
from document import Document
from linkage import Linkage
from artefact import Artefact


class Project(JsonDataClass):

    def __init__(self, path: str):
        self.path = os.path.split(path)[0]
        super().__init__(uid="0", json_path=path)

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

        return cls(path=path)

    def new_document(self, uid: str, title: str) -> Document:
        if uid in self.data["documents"].keys():
            raise Exception("Document uid already in use")
        self.data["documents"][uid] = {"uid": uid}

        return Document.new(self, f"{self.path}//{uid}.json", uid=uid, title=title)

    def open_document(self, stub: str) -> Document:
        return Document(self, stub)

    def find_artefact(self, uid: str) -> Artefact:

        # At some point put lookup cache here

        # Horrible slow code to scan through every doc looking for an artefact
        for doc_name in self.data["documents"]:
            doc = self.open_document(doc_name)
            try:
                art = doc.get_local_artefact(uid)
            except IndexError:
                continue
            else:
                return art

    def find_links(self, art_uid: str) -> List[Linkage]:
        links = []
        # Horrible slow code to scan through every doc looking for an artefact
        for doc_name in self.data["documents"]:
            doc = self.open_document(doc_name)
            links.extend(doc.get_local_artefact_links(art_uid))
        return links

    def new_uid(self) -> str:
        return uuid.uuid4().hex