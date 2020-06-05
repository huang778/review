from Base.base import Base
from page.eleman import EmanPage

class SearchBox(Base):
    # 搜素框
    def send_search_text(self, text):
        self.get_seach(EmanPage.search_input, text)
        # 搜素结果
    def get_search_result(self):
        ruslt = self.ss_eles(EmanPage.search_result)
        return [i.text for i in ruslt]