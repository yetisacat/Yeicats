import json
from API.common.requests_unit import RequestsUnit
from API.common.yaml_unit import write_token_yaml, read_token_yaml


def get_token():
    # 读取 yaml 文件中的 token,设置成全局变量,这边只是做个方法调用, 不做 test 执行.
    global_token = read_token_yaml('token')
    # token 的格式
    token1 = "Bearer" + " " + global_token
    return token1

#创建class 时,也需要设置为 Test
class TestLogining:
    @staticmethod  # 静态方法
    def login(username="bagang", password="BAgang123!", code="520520"):  # 给个默认的账号密码
        global info, jiamidata
        url = "https://hospital.zhenjingai.com/zhenjing-platform/test/sm2/encrypt"
        # 这边是使用 replace函数方法 进行新老数据替换.(将老的字符串全部替换为新的字符串),
        data = '{"data": "{\\"username\\":\\"abcd\\", \\"password\\": \\"bcda\\", \\"code\\":\\"poen\\"}"}'.replace(
            "abcd", username).replace("bcda", password).replace("poen", code)
        headers = {
            'Content-Type': 'application/json'
        }
        # post请求中,data 和 json 只需要传一个
        res1 = RequestsUnit().all_send_request(method="post", url=url, headers=headers, data=data)
        print(res1.json())
        # 验证 http 状态码是否为 200;
        if res1.status_code == 200:
            jiamidata = res1.json()["data"]
            print(f"提取到的jiamidata:{jiamidata}")
        else:
            print(f"接口请求失败,状态码:{res1.status_code}")

        url = "https://hospital.zhenjingai.com/zhenjing-platform/login"
        payload = json.dumps({
            "data": jiamidata  # 获得加密后的 data,这边需要参数化
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = RequestsUnit().all_send_request(method="post", url=url, headers=headers, data=payload)
        print("------分隔符------")
        # 验证 http 状态码是否为 200;
        if response.status_code == 200:
            info = response.json()
            print(f"提取到的info:{info}")
        else:
            print(f"请求失败,状态码:{response.status_code}")

        url = "https://hospital.zhenjingai.com/zhenjing-platform/test/sm2/decrypt"
        data = {
            "data": info
        }
        res2 = RequestsUnit().all_send_request(method="post", url=url, json=data)
        # 返回解密的内容,是字典类型的 str,取 token 很复杂.!!!
        get_token = res2.json()["data"].split('"token":"')[-1][:-2]
        return get_token

    def test_login(self):
        g_token = self.login()
        print("------token------")
        print(g_token)  # 取出 token 作为全局变量
        # 方法一:调用 yaml 的写入方法,将 token 写进 yaml 文件中
        data = {'token': g_token}
        write_token_yaml(data)

        # 方法二: 使用yaml 存储 token
        # yamlpath = r'/Users/zhouxinyao/PycharmProjects/playwright0/API/common/token_g.yaml'
        # token_value = {
        #     'token': g_token
        # }
        # with open(yamlpath, mode="w", encoding="utf-8") as f:
        #     yaml.dump(token_value, f, default_flow_style=False)

