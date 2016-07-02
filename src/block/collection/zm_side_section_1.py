# -*- coding: utf-8 -*-
from src.base.baseitem import BaseItem
from src.tools.match import Match
from src.tools.tag import Tag


class zm_side_section_1(BaseItem):
    u"""
    代表收藏夹右侧的创建者信息

    :param self.raw_avatar:原始头像地址
    :type:unicode
    :param self.avatar:去除size参数后的头像地址
    :type:unicode
    :param self.profile_id:用户主页id
    :type:unicode
    :param self.name:用户名
    :type:unicode
    :param self.headline:用户签名
    :type:unicode
    :param self.hash_id:用户hash_id（w唯一标识符）
    :type:unicode

    测试用例
    resource/block/collection/.zu-main-sidebar .zm-side-section[1]/target.html
    """

    def set_up(self):
        self.parse_raw_creator_avatar()

        creator_dom = self.node.select("#zh-single-answer-author-info")[0]
        self.parse_creator_profile_id(creator_dom)
        self.parse_creator_name(creator_dom)
        self.parse_creator_headline(creator_dom)
        self.parse_creator_hash_id(creator_dom)

        return

    def parse_raw_creator_avatar(self):
        u"""
        dom => self.node
        获取用户头像地址

        :return:link
        :rtype: str
        """
        dom = self.node.select(u"div.zm-side-section-inner a.zm-list-avatar-link")[0]
        img = dom.select(u".zm-list-avatar-medium")[0]
        src = Tag.get_attr(img, u"src")
        self.set_attr("raw_avatar", src)
        avatar = Match.format_avatar(src)
        self.set_attr("avatar", avatar)
        return src

    def parse_creator_profile_id(self, dom):
        u"""
        dom => div#zh-single-answer-author-info
        获取用户profile_id

        :param dom: 用户信息节点
        :type dom: bs4.Tag
        :return:
        :rtype: None
        """
        anchor = dom.select(u"h2.zm-list-content-title a")[0]
        link = Tag.get_attr(anchor, u"href")
        profile_id = Match.match_author_id(link)
        self.set_attr("profile_id", profile_id)
        return

    def parse_creator_name(self, dom):
        u"""
        dom => div#zh-single-answer-author-info
        获取用户名

        :param dom: 用户信息节点
        :type dom: bs4.Tag
        :return:
        :rtype: None
        """
        text_tag = dom.select(u"h2.zm-list-content-title a")[0]
        name = Tag.get_content(text_tag)
        self.set_attr("name", name)
        return

    def parse_creator_headline(self, dom):
        u"""
        dom => div#zh-single-answer-author-info
        获取用户签名

        :param dom: 用户信息节点
        :type dom: bs4.Tag
        :return:
        :rtype: None
        """
        # 签名tag一定存在
        text_tag = dom.select(u"div.zg-gray-normal")[0]

        headline = Tag.get_content(text_tag)
        self.set_attr("headline", headline)
        return

    def parse_creator_hash_id(self, dom):
        u"""
        dom => don#zh-single-answer-author-info
        获取用户hash_id

        :param dom: 用户信息节点
        :type dom: bs4.Tag
        :return:
        :rtype: None
        """
        try:
            follow_button = dom.select(u"button.zm-rich-follow-btn")[0]
        except IndexError:
            # 用户自己的收藏夹
            return
        hash_id = Tag.get_attr(follow_button, u"data-id")
        self.set_attr("hash_id", hash_id)
        return
