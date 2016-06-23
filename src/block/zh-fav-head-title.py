from src.base.base import Base


class zh_fav_head_title(Base):
    def set_up(self):
        title = Base.parse_tools.get_tag_content(self.node)
        self.set_attr("title", title)
        return
