# -*- coding: utf-8 -*-
import unittest
from src.collection import CollectionParser
from test.refer.collection.common import Refer as Common


class CollectionTestCase(unittest.TestCase):
    def setUp(self):
        self.collection_parser = CollectionParser()

        return

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
