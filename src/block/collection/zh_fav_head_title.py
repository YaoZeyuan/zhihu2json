# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.tag import Tag


class zh_fav_head_title(BaseItem):
    u"""
    收藏夹标题
    属性列表：
    self.title

    值    => 含义       => 测试用例
    str   => 收藏夹标题 => resource/block/collection/zh-fav-head-title.html

    """
    def set_up(self):
        title = Tag.get_content(self.node)
        self.set_attr("title", title)
        return
