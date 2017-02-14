# validater
##一个表单验证类，支持int float char re类的验证
* 假如有个表单，需要提交“username” "years" "value" "phone"这四个input
* 其中username为char类，最短为2个长度最长为4个长度，years为int类，在18-30岁之间 value为float类 在0-100之间 phtone为手机号码1开头的11位纯数字
* 先配置一个设置类 继承Validater类

```python
  class FormMyStudent(Validater):
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
            "args": "^1\d{10}$",
            "message": "手机号输入错误",
            "blank": True
        }
  }
```

*  生成实例，直接调用实例的.is_valid()就能判断，若所有输入都符合 数据放在实例的.clear_data里，若有错误，错误提示放在实例的.errors里

```python
  test = FormMyStudent(data)
  if test.is_valid():
    print(test.clear_data, 'ok')
  else:
    print(test.errors, "error")
````
