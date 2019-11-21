from io import StringIO
import sys
import unittest
from src import app
import json
from unittest.mock import patch

from src.app import delete_doc, add_new_doc, get_doc_owner_name, show_all_docs_info

documents = []
directories = {}


def setUpModule():
    with open('../src/fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('../src/fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('src.app.documents', documents, create=True)
@patch('src.app.directories', directories, create=True)
class TestSecretary(unittest.TestCase):

    @patch('src.app.input', return_value='10006')
    def test_delete_doc(self, input_mock):
        start_len = len(documents)
        delete_doc()
        self.assertGreater(start_len, len(documents))

    @patch('src.app.input', return_value='8899')
    @patch('src.app.input', return_value='pasport')
    @patch('src.app.input', return_value='Andrey')
    @patch('src.app.input', return_value='3')
    def test_add_doc(self, input_mock1, input_mock2, input_mock3, input_mock4 ):
        start_len = len(documents)
        add_new_doc()
        self.assertLess(start_len, len(documents))

    @patch('src.app.input', return_value='8899')
    def test_doc_owner(self, input_mock):
        self.assertIsNotNone(get_doc_owner_name())

    def test_show_all_docs_info(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        show_all_docs_info()  # Call unchanged function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(capturedOutput.getvalue())


if __name__ == '__main__':
    unittest.main()
