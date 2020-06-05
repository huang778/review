import pytest

from Base.analysysData import AnalysisData
from Base.driver import Driver
# 统一
from Base.unify import Unify
def get_data():
    # 存储测试数据
    data_list = []
    # 获取yaml文件数据
    data = AnalysisData.get_yaml_data("search.yml")
    for i in data.values():
        data_list.append((i.get("input"), i.get("exp")))
    return data_list

class TestSearch:
    def setup_class(self):
        """声明driver"""
        # 实例化页面类
        # self.sp_obj = SetPage()
        # self.searchbox=SearchBox()
    def teardown_class(self):
        """退出driver"""
        # 引用自定义driver类的退出方法
        Driver.app_teardown()
    @pytest.fixture(scope="class", autouse=True)  # 因为只点击一次搜索按钮 自动运行
    def click_search_btn(self):
        """点击搜索按钮 1次 输入之前运行"""
        # 点击搜索
        Unify.get_search().search_click_btn()

    @pytest.mark.parametrize("search_text,search_result",  get_data())
    def test_search(self, search_text, search_result):
        """内容输入 和 结果断言"""
        # 输入框
        Unify.get_box().send_search_text(search_text)

        # 断言 -列表式断言
        assert search_result in Unify.get_box().get_search_result()