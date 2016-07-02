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
        :type filename:unicode
        :param base_path: 文件路径,不传则默认为self.base_path
        :type base_path: unicode
        :return:解析后的dom元素
        :rtype:bs4.Tag
        """
        if not base_path:
            base_path = self.base_path
        resource_path = base_path + filename
        content = tools.get_content(resource_path)
        dom = tools.parse(content)
        return dom

    #   zh_fav_head_title
    def test_zh_fav_head_title(self):
        from src.block.collection.zh_fav_head_title import zh_fav_head_title

        dom = self.get_dom(u"zh-fav-head-title/title/笑点二代目.html")
        ob = zh_fav_head_title(dom)
        self.assertEqual(ob.get_attr(u"title"), u"""笑点二代目""")
        return

    #   zm_side_section_0
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

    #   zm_side_section_1
    def test_zm_side_section_1(self):
        from src.block.collection.zm_side_section_1 import zm_side_section_1

        dom = self.get_dom(u".zu-main-sidebar .zm-side-section[1]/target.html")
        ob = zm_side_section_1(dom)
        self.assertEqual(ob.get_attr(u"raw_avatar"), u"https://pic2.zhimg.com/cee21b4f469311f5a30b44342dbe6481_m.jpg")
        self.assertEqual(ob.get_attr(u"avatar"), u"https://pic2.zhimg.com/cee21b4f469311f5a30b44342dbe6481.jpg")
        self.assertEqual(ob.get_attr(u"profile_id"), u"I9tm8")
        self.assertEqual(ob.get_attr(u"name"), u"白色潜水艇")
        self.assertEqual(ob.get_attr(u"headline"), u"只唱情歌，看不见坦克。")
        self.assertEqual(ob.get_attr(u"hash_id"), u"a96e3a756f572465e62d75c801f2a717")

        return

if __name__ == '__main__':
    unittest.main()
