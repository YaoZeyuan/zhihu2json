# -*- coding: utf-8 -*-
import json


class Author(object):
    def __init__(self):
        # json数据
        self.json_dict = {}

        # 用户名
        self.name = u''

        # 头像图片id
        self.avatar_id = u''

        # 签名
        self.bio = u''

        # 用户hash值（可用于唯一确定用户身份）
        self.hash = u''

        # 用户个性域名（可以被用户自由修改）
        self.slug = u''

        # 用户描述
        self.description = u''
        return

    def get_dict(self):
        self.json_dict['author'] = self.author.get_dict()
        return self.json_dict

    def get_json(self):
        return json.dumps(self.get_dict())

    def set_name(self, name):
        u"""
        用户昵称
        :param name:
        :return:
        """
        self.name = name
        self.json_dict['name'] = name
        return

    def set_avatar_id(self, avatar_id):
        u"""
        用户头像id
        :param avatar_id:
        :return:
        """
        self.avatar_id = avatar_id
        self.json_dict['avatar_id'] = avatar_id
        return

    def set_bio(self, bio):
        u"""
        用户签名
        :param bio:
        :return:
        """
        self.bio = bio
        self.json_dict['bio'] = bio
        return

    def set_hash(self, hash):
        u"""
        用户唯一标识符:hash

        :param hash:
        :return:
        """
        self.hash = hash
        self.json_dict['hash'] = hash
        return

    def set_slug(self, slug):
        u"""
        用户个性域名地址，通常用做用户id
        :param slug:
        :return:
        """
        self.slug = slug
        self.json_dict['slug'] = slug
        return

    def set_description(self, description):
        """
        用户描述
        :param description:
        :return:
        """
        self.description = description
        self.json_dict['description'] = description
        return
