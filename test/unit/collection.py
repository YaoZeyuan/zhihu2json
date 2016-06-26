# -*- coding: utf-8 -*-
import os
import unittest

from bs4 import BeautifulSoup
from src.block.collection.zh_fav_head_title import zh_fav_head_title
from src.tools.tag import Tag
from test.unit import tools


class CollectionTestCase(unittest.TestCase):
    def setUp(self):
        self.base_resource_path = os.path.split(os.path.realpath(__file__))[0] + "/../resource/block/collection/"
        return

    def test_zh_fav_head_title(self):
        resource_path = self.base_resource_path + "zh-fav-head-title.html"
        content = tools.get_content(resource_path)
        dom = tools.parse(content, "#zh-fav-head-title", 0)
        ob = zh_fav_head_title(dom)
        self.assertEqual(ob.get_attr("title"), u"""

    笑点二代目
""")
        return

if __name__ == '__main__':
    unittest.main()
