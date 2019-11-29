# coding:utf-8
"""
    初始化指定excel文件全路径及文件名称，例如：D:\\case\\template.xlsx，可参考main中的demo
    读取逻辑：共3层循环，分别为：sheet页、行、列，
    先读取所有sheet页，然后在每个sheet页中循环读取行列值放进dict，
    最后汇总到以后数组，
    表头读取，不区分大小写
"""

import xlrd
import public.common_util as util

import public.common_util as temp
class ExcelReadUtil():
    def __init__(self):
        # path = util.convert_path("./case/request_case.xlsx")
        if temp.request_path is None or temp.request_path == "":
            path = util.convert_path("./case/request_case.xlsx")
        else:
            path = util.convert_path(temp.request_path)
        self.data = xlrd.open_workbook(path)
        # 读取所有sheet页
        self.sheets = self.data.sheets()

    def dict_data(self):
        result = []
        for sheet in self.sheets:
            row_values = sheet.row_values(1)
            keys = [s.lower() for s in row_values]
            rowNum = sheet.nrows
            colNum = sheet.ncols
            sheetName = sheet.name
            if rowNum <= 2:
                print("Excel总行数小于2，无法继续执行，停止操作")
            else:
                j = 2
                # 循环读取excel行列值
                for i in list(range(rowNum - 2)):
                    s = {'sheetName': sheetName, 'rowNum': i + 2}
                    # 从第二行还是读取value，第一行是表头不用解析
                    values = sheet.row_values(j)
                    for x in list(range(colNum)):
                        s[keys[x]] = values[x]
                    result.append(s)
                    j += 1
        return result


if __name__ == "__main__":
    data = ExcelReadUtil()
    print(data.dict_data())
