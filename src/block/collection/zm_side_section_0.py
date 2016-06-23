# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.tag import Tag


class zm_side_section_0(BaseItem):
    def set_up(self):
        _class = Tag.get_attr(self.node, "class")
        is_followed = ("zg-btn-white" in _class)
        self.__set_attr("is_followed", is_followed)
        return
