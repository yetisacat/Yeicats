import pytest

# 调用 json 函数来解析 json 字符串
# import json
#
# json_str = '{"name": "Alice", "age": 25}'
# data = json.loads(json_str)  # 将JSON字符串转换为字典或列表
# print(data["name"])  # 输出 Alice
#
# data["city"] = "New York"
# json_str = json.dumps(data)  # 将字典或列表转换为JSON字符串
# print(json_str)  # 输出 {"name": "Alice", "age": 25, "city": "New York"}

class TestData:
#使用方法一:数据驱动格式,args表示参数名,可以根据参数值来自定义.返回结果为 3 次,因为参数值有 3 个.
    # @pytest.mark.parametrize('args',['周一','周二','周三'] )
    # def test_data(self, args):
    #     print(args)

#使用方法二:list 嵌套 list,则表示这是一组参数.参数格式为 list 格式.返回结果以一组来显示,且由参数值来返回执行次数.
    # @pytest.mark.parametrize('args', [['周一', '周二', '周三']])
    # def test_data(self, args):
    #     print(args)

#可以理解为解包操作.
#使用方法三:list嵌套list,由参数值来对应给参数名重命名,返回结果是由参数名来分别对应接收 list里的参数值.有几个就接收几个.
    @pytest.mark.parametrize('name, age', [['周一', 10], ['周二', 11], ['周三', 12]])
    def test_data(self, name, age):
        print(name, age)

#使用方法四:不重新定义参数名,list嵌套list,表示参数值以 list 为一组来传递的.返回结果以一组来显示,且由参数值来返回执行次数.
    # @pytest.mark.parametrize('args', [['周一', 10], ['周二', 11], ['周三', 12]])
    # def test_data(self, args):
    #     print(args)