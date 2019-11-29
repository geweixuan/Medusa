# coding:utf-8
import os
import re
import json


request_path = None

# 路径分隔符转换，将路径匹配当前操作系统。支持windows、linux、mac。不过我只测过windows
def convert_path(path: str) -> str:
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path


""" 将占位符替换为目标值
    实现逻辑：
        1、正则非贪婪模式匹配${与}中间的字符串，因为可能存在多个需要替换的占位符
        2、根据步骤1中提取的关键字，解析替换源（json格式）中的值，实现深层次子孙节点查找
        3、将步骤1中找到的待替换展位符替换为步骤2中找到的值
    例：
        待替换字符串 {"id":"${text.data}","name":${rowNum}}
        替换源{'module': 'moduleA', 'id': 't_002', 'rowNum': 3, 'statuscode': '200', 'text': '{"success":false,"retCode":null,"retMsg":null,"data":"test"}', 'times': '0.003867', 'error': '', 'msg': '', 'result': 'fail'}
        则替换结果为{"id":"test","name":3}
"""


def placeholder_convert(origin, dest):
    if (origin is None) or (dest is None):
        return dest
    result = dest
    for keyword in re.findall(r"\${(.+?)}", result):
        # 查找深层次返回值比如text.content.name
        try:
            temp = json.loads(origin)
        except:
            temp = origin
        for jsonKeyword in keyword.split("."):
            try:
                temp = json.loads(temp.get(jsonKeyword))
            except:
                temp = temp.get(jsonKeyword)

        # 转换成字符串后将占位符替换成目标值，None类型单独处理为空字符串
        if temp is None:
            temp = ""
        result = result.replace("${" + keyword + "}", str(temp))
    return result


if __name__ == "__main__":
    origin = {'module': 'moduleA', 'id': 't_002', 'rowNum': 3, 'statuscode': '200',
              'text': '{"success":false,"retCode":null,"retMsg":null,"data":"test"}', 'times': '0.003867', 'error': '',
              'msg': '', 'result': 'fail'}
    dest = '{"id":"${text.data}","name":${rowNum}}'
    print(placeholder_convert("{'id':'${text}'}", "coffee baby"))
