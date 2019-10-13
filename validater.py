import re


class Validater(object):
    """
    is_valid 是验证方法,会根据传入的dict的key查询在设置类里面的配置,根据相关配置,调用相关方法检测参数是否合格
    合格的参数放入self.clear_data里面,
    不合格的参数,获取相关的错误提示,写入errors里,返回False
    """

    validate = {}

    def __init__(self, request_data):
        self.errors = ""
        self.clear_data = {}
        self.__request_data = request_data

    def is_valid(self):
        is_valid = True
        for (keys, value) in self.__request_data.items():
            if keys in self.validate:
                obj = getattr(self, self.validate[keys]["cate"], None)
                if obj:
                    value = value.strip()
                    is_legal = obj(value, self.validate[keys])
                    if is_legal is False:
                        self.errors = self.validate[keys]["message"]
                    else:
                        self.clear_data[keys] = value
            else:
                self.errors = "%s 为多余值" % value
                is_valid = False
        if self.errors != "":
            is_valid = False
        return is_valid

    def char(self, value, validate_son):
        if value == '':
            if validate_son['blank'] is True:
                return True
            else:
                return False
        else:
            if validate_son["args"]["min"] <= len(value) <= validate_son["args"]["max"]:
                return True
            else:
                return False

    def int(self, value, validate_son):
        if value == '':
            if validate_son["blank"] is True:
                return True
            return False
        try:
            clear_value = int(value)
            if validate_son["args"]["min"] <= clear_value <= validate_son["args"]["max"]:
                return True
            else:
                return False
        except:
            return False

    def float(self, value, validate_son):
        if value == '':
            if validate_son["blank"] is True:
                return True
            return False
        try:
            clear_value = float(value)
            if validate_son["args"]["min"] <= clear_value <= validate_son["args"]["max"]:
                return True
            else:
                return False
        except:
            return False

    def re(self, value, validate_son):
        if value == '':
            if validate_son["blank"] is True:
                return True
            return False
        m = re.search(validate_son['args'], value)
        if m:
            return True
        else:
            return False


class FormMyStudent(Validater):
    """ 设置类
        继承Validater类,

        cate:是验证类型
        args:是验证方法
        message:错误提示方法
        blank:是否允许为空白输入 True是允许空白输入 False是不允许空白输入
    """
    validate = {
        "username": {
            "cate": "char",
            "args": {"max": 4, "min": 2},
            "message": "姓名输入错误",
            "blank": False
        },
        "years": {
            "cate": "int",
            "args": {"max": 30, "min": 18},
            "message": "年龄输入错误",
            "blank": False
        },
        "value": {
            "cate": "float",
            "args": {"max": 100, "min": 0},
            "message": "成绩输入错误",
            "blank": False
        },
        "phone": {
            "cate": "re",
            "args": '^1\d{10}$',
            "message": "手机号输入错误",
            "blank": True

        }
    }

if __name__ == '__main__':
    '''测试'''
    data1 = {"username": '王', 'years': '20', 'value': '80', "phone": '18799999999'}
    data2 = {"username": 'w', 'years': '21', 'value': '80', "phone": '18799999999'}
    data3 = {"username": 'w', 'years': '21', 'value': '80', "phone": ''}

    data4 = {"username": 'w', 'years': '21', 'value': '', "phone": '18799999999'}
    data5 = {"username": 'w', 'years': '20', 'value': '80', "phone": '18799999999', 'a': 'b'}
    data6 = {"username": 'wl00op0o', 'years': '20', 'value': 'phone', "key": '18799999999'}
    data7 = {"username": '王', 'years': '200', 'value': '80', "phone": '18799999999'}
    data8 = {"username": '王', 'years': '20', 'value': '-1', "phone": '18799999999'}
    data9 = {"username": '王', 'years': '20.9', 'value': '80', "phone": '18799999999'}
    data10 = {"username": '王', 'years': '20', 'value': '', "phone": '18799999999'}
    data11 = {"username": '王', 'years': '20', 'value': '80', "phone": '18799999999'}
    all_data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]
    for data in all_data:
        test = FormMyStudent(data)
        if test.is_valid():
            print(test.clear_data, 'ok')
        else:
            print(test.errors, "error")
