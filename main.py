import unittest
from unittest.mock import patch
import directories
from test_yandex_api import Yandex_Request

class TestDirectories(unittest.TestCase):

    def test_get_doc_shelf(self):
        self.assertEqual(directories.get_doc_shelf('11-2'), '1')

    def test_get_doc_owner_name(self):
        self.assertEqual(directories.get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_remove_doc_from_shelf(self):
        self.assertEqual(directories.remove_doc_from_shelf('11-2'), {
            '1': ['2207 876234', '5455 028765'],
            '2': ['10006'],
            '3': []
        })

    def test_yandex_api(self):
        yandex_test = Yandex_Request('AgAAAAAnT4gjAADLWxNiaFqSQk1Zl4YxP-nbi5o')
        self.assertEqual(yandex_test.create_folder('https://cloud-api.yandex.net:443/v1/disk/resources'), 201)

if __name__ == '__main__':
    unittest.main()