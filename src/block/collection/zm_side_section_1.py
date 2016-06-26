# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.tag import Tag


class zm_side_section_0(BaseItem):
    u"""
    代表收藏夹右侧的创建者信息

    :param self.is_self:是否是用户自己创建的收藏夹
    :type:boolean
    测试用例
    True => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_has_followed.html
    False => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_not_followed.html

    :param self.is_followed:是否已关注
    :type:boolean
    测试用例
    True => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_has_followed.html
    False => resource/block/collection/.zu-main-sidebar .zm-side-section[0]_not_followed.html

    :param self.:
    """

    def set_up(self):
        follow_button = self.node.select(u"a.zu-entry-focus-button")[0]
        _class = Tag.get_attr(follow_button, u"class")
        is_followed = (u"zg-btn-white" in _class)
        self.set_attr(u"is_followed", is_followed)
        return
