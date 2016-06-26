# -*- coding: utf-8 -*-
import unittest

from test.unit import tools
from test.unit.config import Config


class CollectionTestCase(unittest.TestCase):
    def setUp(self):
        self.base_path = Config.base_path + u"/../resource/block/collection/"
        return

    def get_dom(self, filename, base_path=None):
        u"""
        封装tools操作，快速获取解析后的dom元素

        :param filename:文件名(base_path为默认值)
        :type filename:str
        :param base_path: 文件路径,不传则默认为self.base_path
        :type base_path: str
        :return:解析后的dom元素
        :rtype:bs4.Tag
        """
        if not base_path:
            base_path = self.base_path
        resource_path = base_path + filename
        content = tools.get_content(resource_path)
        dom = tools.parse(content)
        return dom

    def test_zh_fav_head_title(self):
        from src.block.collection.zh_fav_head_title import zh_fav_head_title

        dom = self.get_dom(u"zh-fav-head-title/title/笑点二代目.html")
        ob = zh_fav_head_title(dom)
        self.assertEqual(ob.get_attr(u"title"), u"""笑点二代目""")
        return

    def test_zm_side_section_0_has_followed(self):
        from src.block.collection.zm_side_section_0 import zm_side_section_0

        dom = self.get_dom(u".zu-main-sidebar .zm-side-section[0]/is_followed/true.html")
        ob = zm_side_section_0(dom)
        self.assertEqual(ob.get_attr(u"is_followed"), True)
        return

    def test_zm_side_section_0_not_followed(self):
        from src.block.collection.zm_side_section_0 import zm_side_section_0

        dom = self.get_dom(u".zu-main-sidebar .zm-side-section[0]/is_followed/false.html")
        ob = zm_side_section_0(dom)
        self.assertEqual(ob.get_attr(u"is_followed"), False)
        return


if __name__ == '__main__':
    unittest.main()
