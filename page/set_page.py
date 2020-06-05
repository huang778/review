from Base.base import Base
from page.eleman import EmanPage

class SetPage(Base):
    def __init__(self):
        super().__init__()
         #实例化base类
         # self.base=Base()
         # 定义点击搜素
         # self.btn=(By.ID,"com.android.settings:id/search")
         # # 定义输入框
         # self.input=(By.ID,"android:id/search_src_text")
         # # 定义返回结果
         # self.ruslt=(By.ID,"com.android.settings:id/title")
         # 点击搜素
        # 设置页面
        # 搜素按钮
    def search_click_btn(self):
          self.click_btn( EmanPage.search_btn)

