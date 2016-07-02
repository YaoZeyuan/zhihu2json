# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.match import Match
from src.tools.tag import Tag


class zm_side_section_2(BaseItem):
    u"""
    代表收藏夹右侧的收藏夹状态

    :param self.update_date:最近更新日期
    :type:unicode
    :param self.follower_count:关注者总数
    :type:unicode
    :param self.collection_id:收藏夹id
    :type:unicode

    测试用例
    resource/block/collection/.zu-main-sidebar .zm-side-section[2]/target.html
    """

    def set_up(self):
        self.parse_update_date()
        self.parse_follower_count()
        self.parse_collection_id()
        return

    def parse_update_date(self):
        u"""
        获取最近更新日期
        """
        dom = self.node.select(u"div.zg-gray-normal span.time")[0]
        raw_update_date = Tag.get_content(dom)
        update_date = Match.parse_date(raw_update_date)
        self.set_attr("update_date", update_date)
        return

    def parse_follower_count(self):
        u"""
        获取关注人数
        """
        dom = self.node.select(u'div.zg-gray-normal a[data-za-l="collection_followers_count"]')[0]
        follower_count = Tag.get_content(dom)
        self.set_attr("follower_count", follower_count)
        return

    def parse_collection_id(self):
        u"""
        获取收藏夹id
        """
        anchor = self.node.select(u'div.zg-gray-normal a[data-za-l="collection_followers_count"]')[0]
        log_src = Tag.get_attr(anchor, u"href")
        collection_id = Match.match_collection_id(log_src)
        self.set_attr("collection_id", collection_id)
        return
