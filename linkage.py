
# Library imports
from typing import TYPE_CHECKING

# Project imports
if TYPE_CHECKING:
    from project import Project
    from document import Document
from artefact import Artefact


class Linkage:
    def __init__(self, document: 'Document', uid: str):
        self.data = [link for link in document.data["linkage"] if link["uid"] == uid][0]

    @classmethod
    def new(cls, uid: str, source_artefact: 'Artefact', destination_artefact: 'Artefact', link_type: str):

        data = {"uid": uid,
                "type": link_type,
                "source":       {"document": {"uid": source_artefact.document.uid},
                                 "artefact": {"uid": source_artefact.uid}
                                 },
                "destination":  {"document": {"uid": destination_artefact.document.uid},
                                 "artefact": {"uid": destination_artefact.uid}
                                 }
                }

        source_artefact.document.data["linkage"].append(data)

        return cls(source_artefact.document, uid)

    @property
    def source(self) -> Artefact:
        return Artefact(self.data["source"])

    @property
    def destination(self) -> Artefact:
        return Artefact(self.project)
