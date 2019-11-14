#coding=utf-8
import abc
class Test:
    @abc.abstractmethod
    def run(self):
        return

class RequestTest(Test):
    def getCase(self):
        print("RequestTest 正在读取用例")
    def runTest(self):
        print("RequestTest 正在执行用例")
    def run(self):
        self.getCase()
        self.runTest()

class SeleniumTest(Test):
    def getCase(self):
        print("SeleniumTest 正在读取用例")
    def runTest(self):
        print("SeleniumTest 正在执行用例")
    def run(self):
        self.getCase()
        self.runTest()