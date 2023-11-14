
# Library imports
from typing import TYPE_CHECKING
import functools

# Project imports
from base import Base
from linkage import Linkage
if TYPE_CHECKING:
    from document import Document


def _autosave(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        ret = f(*args, **kwargs)
        args[0].document.save()
        return ret
    return wrapper


class Artefact(Base):

    def __init__(self, uid: str, document: 'Document'):
        super().__init__(uid)
        self.document = document
        self._data = [d for d in self.document.data["content"] if d["uid"] == self.uid][0]

    @classmethod
    def new(cls, document: 'Document', uid: str, content: str, index: int):
        document.data["content"].insert(index, {"uid": uid, "content": content})
        document.save()
        return cls(uid=uid, document=document)

    @property
    def content(self):
        return self._data.get("content", None)

    @content.setter
    @_autosave
    def content(self, new_content: str):
        self._data["content"] = new_content

    @property
    def type(self):
        return self._data.get("type", None)

    @type.setter
    @_autosave
    def type(self, new_type: str):
        self._data["type"] = new_type

    def link_to(self, other_artefact: 'Artefact', link_type: str) -> Linkage:
        return Linkage.new(uid=self.document.new_uid(), source_artefact=self,
                           destination_artefact=other_artefact, link_type=link_type)

