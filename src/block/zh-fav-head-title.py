from src.base.base import Base


class zh_fav_head_title(Base):
    def __init__(self, node):
        super(zh_fav_head_title, self).__init__(node)
        self.title = ""
        self.set_up()
        return

    def set_up(self):
        title = Base.parse_tools.get_tag_content(self.node)
        self.__set_attr("title", title)
        return
