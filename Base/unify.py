from page.Searchbox import SearchBox
from page.set_page import SetPage
class Unify:
    @classmethod
    def get_search(self):
        return  SetPage()
    @classmethod
    def get_box(self):
        return  SearchBox()