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
        follow_button = self.node.select(u"a.zu-entry-focus-button")[0]
        _class = Tag.get_attr(follow_button, u"class")
        is_followed = (u"zg-btn-white" in _class)
        self.set_attr(u"is_followed", is_followed)
        return
