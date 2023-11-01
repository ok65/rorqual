
# Library imports
from typing import TYPE_CHECKING

# Project imports
if TYPE_CHECKING:
    from project import Project
from artefact import Artefact


class Linkage:
    def __init__(self, project: 'Project', uid: str):
        self.project = project
        self.data = [link for link in project.data["links"] if link["uid"] == uid][0]

    @classmethod
    def new(cls, project: 'Project', source: 'Artefact', destination: 'Artefact', link_type_uid: str):
        linkage = {"uid": project.new_uid(), "source": source._id, "destination": destination._id,
                   "link_type_uid": link_type_uid}
        project.data["links"].append(linkage)

        return cls(project, linkage["uid"])

    @property
    def source(self) -> Artefact:
        return Artefact(self.project)