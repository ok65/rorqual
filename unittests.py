
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

    def test_find_links(self):
        doc1 = self.project.new_document("D1", "Red")
        doc2 = self.project.new_document("D2", "Blue")
        doc3 = self.project.new_document("D3", "Green")

        parent_art = doc1.new_artefact("Parent Artefact")

        blue_art = doc2.new_artefact("Blue Artefact 1")
        green_art1 = doc3.new_artefact("Green Artefact 1")
        green_art2 = doc3.new_artefact("Green Artefact 2")

        doc2.new_linkage(source_artefact=blue_art, destination_doc_uid=doc1.uid,
                         destination_art_uid=parent_art.uid, link_type="Simple Link")

        doc3.new_linkage(source_artefact=green_art1, destination_doc_uid=doc1.uid,
                         destination_art_uid=parent_art.uid, link_type="Simple Link")

        doc3.new_linkage(source_artefact=green_art2, destination_doc_uid=doc1.uid,
                         destination_art_uid=parent_art.uid, link_type="Simple Link")

        links = self.project.find_links(parent_art.uid)

        self.assertEqual(len(links), 3)

        self.assertEqual(links[0].destination_uid, parent_art.uid)


class DocumentTests(RorqualTestBase):

    def test_new_document(self):
        TITLE = "apples"
        UID = "APL"

        doc = self.project.new_document(uid=UID, title=TITLE)

        self.assertIsInstance(doc, Document)
        self.assertEqual(doc.title, TITLE)

    def test_new_artefact(self):
        doc = self.project.new_document(uid="apl", title="Apples")
        self.assertEqual(len(doc.get_local_artefact_list()), 0)
        art = doc.new_artefact("Test artefact")
        self.assertEqual(len(doc.get_local_artefact_list()), 1)

    def test_move_artefact(self):
        doc = self.project.new_document(uid="apl", title="Apples")
        doc.new_artefact("Second")
        doc.new_artefact("Third")
        first = doc.new_artefact("First")
        self.assertEqual(doc.get_local_artefact_list()[-1].content, "First")
        doc.move_artefact(first.uid, 0)
        self.assertEqual(doc.get_local_artefact_list()[-1].content, "Third")
        pass

    def test_create_linkage(self):
        doc1 = self.project.new_document(uid="doc1", title="document 1")
        doc2 = self.project.new_document(uid="doc2", title="document 2")

        source_art = doc1.new_artefact("Apples")
        dest_art = doc2.new_artefact("Oranges")

        link = doc1.new_linkage(source_artefact=source_art, link_type="relation",
                                destination_doc_uid=doc2.uid, destination_art_uid=dest_art.uid)

        self.assertEqual(link.source_uid, source_art.uid)
        self.assertEqual(link.destination_uid, dest_art.uid)
        self.assertEqual(link.source_document_uid, doc1.uid)
        self.assertEqual(link.destination_document_uid, doc1.uid)

    def test_properties(self):
        TITLE = "apples"
        doc = self.project.new_document(uid="apl", title=TITLE)
        self.assertEqual(doc.title, TITLE)
        doc.title = TITLE = "oranges"
        self.assertEqual(doc.title, TITLE)