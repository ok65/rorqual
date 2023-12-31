
# Library imports
from typing import TYPE_CHECKING

# Project imports
from posix_dict import PosixDict
if TYPE_CHECKING:
    from project import Project
    from document import Document
    from artefact import Artefact


class Linkage:
    def __init__(self, document: 'Document', uid: str):
        self.data = document.data.cut(f"linkage/{uid}")

    @classmethod
    def new(cls, uid: str, source_artefact: 'Artefact', destination_doc_uid, destination_art_uid: 'str', link_type: str):

        data = {"uid": uid,
                "type": link_type,
                "source":       {"document": {"uid": source_artefact.document.uid},
                                 "artefact": {"uid": source_artefact.uid}
                                 },
                "destination":  {"document": {"uid": destination_doc_uid},
                                 "artefact": {"uid": destination_art_uid}
                                 }
                }

        source_artefact.document.data[f"linkage/{uid}"] = PosixDict(data)

        return cls(source_artefact.document, uid)

    @property
    def source_uid(self) -> 'str':
        return self.data["source/artefact/uid"]

    @property
    def destination_uid(self) -> 'str':
        return self.data["destination/artefact/uid"]

    @property
    def source_document_uid(self):
        return self.data["source/document/uid"]

    @property
    def destination_document_uid(self):
        return self.data["source/document/uid"]
