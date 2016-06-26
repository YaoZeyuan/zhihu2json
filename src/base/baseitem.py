# -*- coding: utf-8 -*-


class BaseItem(object):
    u"""
    基础类，用于提供通用的框架
    """
    def __init__(self, node):
        u"""
        初始化节点
        初始化对象及属性值
        :param node:
        :return:
        """
        #   节点元素
        self.node = node

        #   属性字典
        self.attr_dict = {}

        #   对象名
        self.class_name = u"base"

        #   初始化属性值
        self.set_up()
        return

    def set_up(self):
        """
        初始化属性值
        :rtype: None
        """
        return

    def tear_down(self):
        """
        清空记录，以便重新计算
        :rtype: None
        """
        self.attr_dict = {}
        self.node = None
        return

    def set_node(self, node):
        u"""
        重置节点
        :param node:
        :rtype: None
        """
        self.tear_down()
        self.node = node
        self.set_up()
        return

    def set_attr(self, name, value):
        setattr(self, name, value)
        self.attr_dict[name] = value
        return

    def get_attr(self, attr):
        u"""
        获取指定属性
        如果没有对应属性，抛出异常，异常内容：『class_name中没有attr属性，请检查后再试』
        :param attr:
        :return string:
        """

        if attr not in self.attr_dict:
            raise Exception(u"{}对象中没有{}属性".format(self.class_name, attr))
        return self.attr_dict.get(attr, "")

    def get(self):
        return self.attr_dict
