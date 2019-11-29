# coding:utf-8
import unittest
from ddt import ddt, data
import requests
from public.excel2case import ExcelReadUtil
from public import common_util as placeholderUtil, request2result
import json

testData = ExcelReadUtil().dict_data()
dependencyData = globals()
dependencyData = {}


@ddt
class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录，就在这里先登录 todo

    @data(*testData)
    def test_api1(self, data):
        print("-----------%s-----------" % data)
        if data["是否运行"] == "YES":
            if data["case依赖"] != "":
                try:
                    # 处理参数、url中的占位符
                    data["params"] = placeholderUtil.placeholder_convert(json.dumps(dependencyData[data["case依赖"]]), data["params"])
                    data["url"] = placeholderUtil.placeholder_convert(json.dumps(dependencyData[data["case依赖"]]), data["url"])
                except Exception as msg:
                    print("依赖数据处理失败 :%s" % msg)
            else:
                pass
            res = request2result.send_requests(self.s, data)
            # 检查点 checkpoint
            check = data["checkpoint"]
            print("检查点->：%s" % check)
            # 返回结果
            res_text = res["text"]
            print("返回实际结果->：%s" % res_text)
            # 保存运行结果，实现用例依赖
            try:
                dependencyData[data["id"]] = res
            except:
                pass
            # 断言 todo 可以扩展断言方式，全文匹配or模糊匹配等
            self.assertTrue(check in res_text)


if __name__ == "__main__":
    unittest.main()
