from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver


class Base:
    def __init__(self):
        # 启动参数
        self.driver=Driver.app_driver()
           # 定位单个元素方法
    def ss_ele(self,kk,timeout=5,poll_frequency=1.0):
        """
        :param kk:元组 定位元素的方法
        :param timeout: 元素打开时间
        :param poll_frequency:  元素间隔
        :return: 返回元素方法
        """
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*kk))
    # 定位一组元素方法
    def ss_eles(self,kk,timeout=5,poll_ferquency=1.0):
        """
        :param kk:
        :param timeout:
        :param poll_ferquency:
        :return:
        """
        return WebDriverWait(self.driver,timeout,poll_ferquency).until(lambda x:x.find_elements(*kk))
    # 定位点击搜素按钮方法
    def click_btn(self,kk,timeout=5,poll_ferquency=1.0):
        self.ss_ele(kk,timeout,poll_ferquency).click()
    # 定位搜素输入方法
    def get_seach(self,kk,text,timeout=5,poll_ferquency=1.0):
        qq=self.ss_ele(kk,timeout,poll_ferquency)
        qq.clear()
        qq.send_keys(text)

if __name__ == '__main__':
     base=Base()
     # 定位搜素按钮 "com.android.settings:id/search"
     btn=(By.ID,"com.android.settings:id/search")
     base.click_btn(btn)
     # 定位搜素输入"android:id/search_src_text"
     seach=(By.ID,"android:id/search_src_text")
     base.get_seach(seach,"i")
     # 定位搜素结果 "com.android.settings:id/title"
     get_seach=(By.ID,"com.android.settings:id/title")
     ruslt=base.ss_eles(get_seach)
     print("结果为:",[i.text for i in ruslt])









