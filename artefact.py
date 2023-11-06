
# Library imports
from typing import TYPE_CHECKING

# Project imports
from base import Base
if TYPE_CHECKING:
    from document import Document


class Artefact(Base):

    def __init__(self, uid: str, document: 'Document'):
        super().__init__(uid)
        self.document = document
        self._data = [d for d in self.document.data["content"] if d["uid"] == self.uid][0]

    @classmethod
    def new(cls, document: 'Document', uid: str, content: str, index: int):
        document.data["content"].insert(index, {"uid": uid, "content": content})
        return cls(uid=uid, document=document)

    @property
    def content(self):
        return self._data.get("content", None)

    @content.setter
    def content(self, content: str):
        self._data["content"] = content

    @property
    def type(self):
        return self._data.get("type", None)

    @type.setter
    def type(self, type: str):
        self._data["type"] = type
