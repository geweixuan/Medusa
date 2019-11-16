# coding:utf-8
import unittest
import ddt
import os
import requests
from public.request_utils import request2result
from public.excel_utils.excel2case import ExcelReadUtil
import conf.global_param as CONSTANTS


testdata = ExcelReadUtil(CONSTANTS.REQUEST_EXECUTE_FILE_NAME).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录，就在这里先登录 todo

    @ddt.data(*testdata)
    def test_api(self, data):
        res = request2result.send_requests(self.s, data)
        # 检查点 checkpoint
        check = data["checkpoint"]
        print("检查点->：%s"%check)
        # 返回结果
        res_text = res["text"]
        print("返回实际结果->：%s"%res_text)
        # 断言 todo 可以扩展断言方式，全文匹配or模糊匹配等
        self.assertFalse(check in res_text)

if __name__ == "__main__":
    unittest.main()
