#coding:utf-8
'''闹着玩的，输出换个字体颜色，info-绿色，warn-黄色，error-红色'''

import os
def convert_path(path: str) -> str:
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path