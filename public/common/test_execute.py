# coding=utf-8
import abc
import unittest
from public.html_test_utils import html_test_runner_api
import os
import time
import public.common.common_util as path_util
import conf.global_param as CONSTANTS


class Test:
    def __init__(self):
        self.report_path = path_util.convert_path(CONSTANTS.PROJECT_PATH + "report/")
        if not os.path.exists(self.report_path): os.mkdir(self.report_path)
        self.case_path = path_util.convert_path(CONSTANTS.PROJECT_PATH + "case/")

    @abc.abstractmethod
    def run(self):
        return


class RequestTest(Test):
    def getCase(self, rule="test*.py"):
        print("RequestTest 正在读取 %s 用例" % self.case_path)
        discover = unittest.defaultTestLoader.discover(self.case_path, pattern=rule)
        return discover

    def runTest(self, all_case):
        print("RequestTest 正在执行用例")
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        htmlreport = self.report_path + r"RequestTestResult_" + now + r".html"
        print("测试报告生成地址：%s" % htmlreport)
        fp = open(htmlreport, "wb")
        runner = html_test_runner_api.HTMLTestRunner(stream=fp,
                                                     verbosity=2,
                                                     title="Medusa RequestTest测试报告",
                                                     description="接口用例执行情况")
        runner.run(all_case)
        fp.close()

    def run(self):
        self.runTest(self.getCase())


class SeleniumTest(Test):
    def getCase(self):
        print("SeleniumTest 正在读取用例")

    def runTest(self):
        print("SeleniumTest 正在执行用例")

    def run(self):
        self.runTest(self.getCase())
