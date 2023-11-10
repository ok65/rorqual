
# Library imports
import unittest
import os
import shutil

# Project imports
from project import Project
from document import Document

TESTPATH = "test"
PROJPATH = f"{TESTPATH}//test_project.json"


class RorqualTestBase(unittest.TestCase):

    def setUp(self) -> None:

        # Purge existing test folder
        if os.path.exists(TESTPATH):
            shutil.rmtree(TESTPATH)

        # Create new empty test folder
        os.mkdir(TESTPATH)

        # Create new project
        self.project = Project.new(PROJPATH)

    def tearDown(self) -> None:

        # Destroy project instance
        if hasattr(self, "project"):
            del self.project

        # Purge test folder
        if os.path.exists(TESTPATH):
            shutil.rmtree(TESTPATH)


class ProjectTests(RorqualTestBase):

    def test_new_project(self):
        self.assertIsInstance(self.project, Project)

    def test_find_artefact(self):
        fruit_doc = self.project.new_document("D1", "Fruit")
        art1 = fruit_doc.new_artefact("Fruit must grow on tree or bush")
        art2 = self.project.find_artefact(art1.uid)
        self.assertEqual(art1.content, art2.content)


class DocumentTests(RorqualTestBase):

    def test_new_document(self):
        TITLE = "apples"
        UID = "APL"

        doc = self.project.new_document(uid=UID, title=TITLE)

        self.assertIsInstance(doc, Document)
        self.assertEquals(doc.title, TITLE)

    def test_new_artefact(self):
        doc = self.project.new_document(uid="apl", title="Apples")
        self.assertEqual(len(doc.get_artefact_list()), 0)
        art = doc.new_artefact("Test artefact")
        self.assertEqual(len(doc.get_artefact_list()), 1)

    def test_properties(self):
        TITLE = "apples"
        doc = self.project.new_document(uid="apl", title=TITLE)
        self.assertEqual(doc.title, TITLE)
        doc.title = TITLE = "oranges"
        self.assertEqual(doc.title, TITLE)