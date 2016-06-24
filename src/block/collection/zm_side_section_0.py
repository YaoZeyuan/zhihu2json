# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.tag import Tag


class zm_side_section_0(BaseItem):
    u"""
    代表收藏夹右侧的『关注/取消关注』按钮
    属性列表：
    self.is_followed

    值    => 含义   => 测试用例
    True  => 已关注 => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_has_followed.html
    False => 未关注 => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_not_followed.html

    """
    def set_up(self):
        _class = Tag.get_attr(self.node, "class")
        is_followed = ("zg-btn-white" in _class)
        self.__set_attr("is_followed", is_followed)
        return
