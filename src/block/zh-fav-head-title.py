from src.base.baseitem import BaseItem
from src.tools.tag import Tag


class zh_fav_head_title(BaseItem):
    def set_up(self):
        title = Tag.get_content(self.node)
        self.__set_attr("title", title)
        return
