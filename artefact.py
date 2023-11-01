
# Library imports
from typing import TYPE_CHECKING, Dict

# Project imports
if TYPE_CHECKING:
    from document import Document


class Artefact:

    def __init__(self, document: 'Document', _id: int):
        self._document = document
        self._id = _id
        self._data = [d for d in self._document.data["content"] if d["id"] == self._id][0]

    @property
    def content(self):
        return self._data.get("content", None)

    @content.setter
    def content(self, content: str):
        self._data["content"] = content

