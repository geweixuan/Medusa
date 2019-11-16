#coding:utf-8
'''
    初始化指定excel文件全路径及文件名称，例如：D:\\case\\template.xlsx，可参考main中的demo
    读取逻辑：共3层循环，分别为：sheet页、行、列，
    先读取所有sheet页，然后在每个sheet页中循环读取行列值放进dict，
    最后汇总到以后数组
'''
import xlrd
import public.common.common_util as util
from conf import global_param as CONSTANTS
class ExcelReadUtil():
    def __init__(self, excel_name):
        if excel_name == "":
            util.error("异常退出，未指定读取excel文件名称！")
        path = util.convert_path(CONSTANTS.PROJECT_PATH + "/case/requests/" + excel_name)
        self.data = xlrd.open_workbook(path)
        #读取所有sheet页
        self.sheets = self.data.sheets()
    def dict_data(self):
        result = []
        for sheet in self.sheets:
            keys = sheet.row_values(0)
            rowNum = sheet.nrows
            colNum = sheet.ncols
            sheetName = sheet.name
            if rowNum <= 1:
                util.error("Excel总行数小于1，无法继续执行，停止操作")
            else:
                j = 1
                #循环读取excel行列值
                for i in list(range(rowNum - 1)):
                    s = {}
                    #从第二行还是读取value，第一行是表头不用解析
                    s['sheetName'] = sheetName
                    s['rowNum'] = i + 2
                    values = sheet.row_values(j)
                    for x in list(range(colNum)):
                        s[keys[x]] = values[x]
                    result.append(s)
                    j += 1
        return result
if __name__ == "__main__":
    data = ExcelReadUtil("template.xlsx")
    print(data.dict_data())