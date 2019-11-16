# coding:utf-8
import json
import requests

from public.excel_utils.excel2case import ExcelReadUtil


def send_requests(session, testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    # 请求头部header todo 自动token
    try:
        headers = eval(testdata["headers"])
        print("请求头部：%s" % headers)
    except:
        headers = None
    # post 请求body类型
    type = testdata["type"]
    test_moudle = testdata["sheetName"]
    test_nub = testdata["id"]
    print("=======正在执行用例：%s - %s========" % (test_moudle, test_nub))
    print("请求方式：%s, 请求url: %s" % (method, url))
    print("请求params：%s" % params)

    # post 请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = []

    # 判断传data数据还是json,todo 扩展body类型
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "POST": print("post请求body类型为：%s ,body内容为：%s" % (type, body))

    verify = False
    res = {}  # 接受返回数据

    try:
        r = session.request(method=method,
                            url=url,
                            params=params,
                            headers=headers,
                            data=body,
                            verify=verify
                            )
        print("请求返回信息：%s" % r.content.decode("utf-8"))
        res['module'] = testdata['sheetName']
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())  # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res


if __name__ == "__main__":
    from public.excel_utils.excel2case import ExcelReadUtil as ReadExcel

    data = ReadExcel("template.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s, data[0])
    print(res)
