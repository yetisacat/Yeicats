# 读取 yaml 文件的方法
import os
import pytest
import yaml


# os.getcwd()  这是根目录的意思

# 读取测试用例数据的方法:传入 yaml_name名字:shuju_data.yaml
def read_shuju_yaml(path):
    with open(path, mode='r',encoding="utf-8") as f:
        shuju = yaml.load(stream=f, Loader=yaml.FullLoader)
        return shuju

# 实际调用读取数据方法, 是以执行的 py 文件为目标去找路径.
# if __name__ == '__main__':
#     print(read_shuju_yaml("./shuju_data.yaml"))


# 读取 yaml 文件方式,使用 key 值来获取 value 值; 不加 key 则是读取全部,每执行一次只会生成一个 token,因为会被覆盖掉.
# 读取 token:
def read_token_yaml(key):
    with open("/Users/zhouxinyao/PycharmProjects/playwright0/API/global_token.yaml", mode='r', encoding="utf-8") as f:
        token = yaml.load(stream=f, Loader=yaml.FullLoader)
        # print(token[key])
        return token[key]


#    token写入 yaml 文件方式:
def write_token_yaml(data):
    with open("/Users/zhouxinyao/PycharmProjects/playwright0/API/global_token.yaml", mode='w', encoding="utf-8") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 追加写入 yaml 文件方式: 这边的 mode= a ,表示 append,但是执行后都会重复追加,若多个数据进行写入, 可以先清除再使用追加方式.
# def write_token_yaml1(self, data):
#     with open(os.getcwd() + "/API/common/token_g.yaml", mode='a', encoding="utf-8") as f:
#         yaml.dump(data=data, stream=f, allow_unicode=True)

# 清除 yaml 文件方法:
def clear_token_yaml():
    with open("/Users/zhouxinyao/PycharmProjects/playwright0/API/common/token_g.yaml", mode='w', encoding="utf-8") as f:
        f.truncate()

# 使用绝对路径读取 yaml 数据
# f = open("/Users/zhouxinyao/PycharmProjects/playwright0/API/common/token_g.yaml", "r", encoding="utf-8")
# data = f.read()
# print(data['value'])
# ydata = yaml.loader(data)
# print(ydata)

# yaml_path ='/Users/zhouxinyao/PycharmProjects/playwright0/API/common/token_g.yaml'
# '{"msg":"操作成功","code":200,"token":"eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjYyNDZlMjMwLTMyZDAtNDFmMS1iMzljLWJiMzY4NWI1NjZhZSJ9.8BSlVj8pkuh_7UaL4d0qtevZgdrznOlqRMI1tAuIbPtuWirqvCylnQtttZdRsgy1GpTzoyvRyWxG45TsEPn68A"}'.split('"token":"')[-1][:-2]
