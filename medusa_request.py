#coding=utf-8
from public.test_execute import RequestTest
import os
import public.common_util as temp
# 自动化接口测试执行
requestPath = input('请输入用例全路径: ')
temp.request_path = requestPath
test = RequestTest()
test.run()

os.system("pause")