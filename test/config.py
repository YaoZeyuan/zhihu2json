# -*- coding: utf-8 -*-

#   使用importlib按字符串导入包
#   demo => importlib.import_module('matplotlib.text')
u"""
模板：

config => {
    "resource" => {
        "一级目录" => {
            "二级目录" => {
                "n级目录" => {
                    "类文件名(不含扩展名)" => {
                        "target" => "待导入类名",
                        "test_suite" => [
                        {
                            "name" => "测试用例1",
                            "desc" => "测试用例1描述信息",
                            "detect" => [
                            {
                                "attr" => "属性名"
                                "correct_value" => "正确的解析值"
                            },
                            {
                                "attr" => "属性名"
                                "correct_value" => "正确的解析值"
                            },
                            ]
                        },
                        {
                            "name" => "测试用例2",
                            "desc" => "测试用例2描述信息",
                        },
                        {
                            "name" => "测试用例n",
                            "desc" => "测试用例n描述信息",
                        },
                        ]
                    }
                }
            }
        }


    }
}
"""
config = {
    "resource":
        {
            "block": {
                "ajax": {

                },
                "collection": {
                    "zh_fav_head_title": {
                        "target": "zh_fav_head_title",  # 待导入文件
                        "test_suite": [{
                            "name": "zh-fav-head-title.html",
                            "desc": "收藏夹标题",
                        },
                        ]
                    },
                    "zm_side_section_0": {
                        "target": "zm_side_section_0",  # 待导入类名
                        "test_suite": [{
                            "name": "zh-fav-head-title.html",
                            "desc": "收藏夹标题",
                        },
                        ]
                    },
                },
            },
        },
}
