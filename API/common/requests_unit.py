#统一封装请求
import json

import requests


class RequestsUnit:
    # 建立统一session会话,且在每个执行方法中调用统一会话,调用的时候不要忘记()
    session = requests.session()  # 写法二:设置为全局的类变量

    # def get_seesion(self):      #写法一,这样写的话,每调用一次,session 会重新生成一次.接口可能会有失败的风险.
    #     session = requests.session()
    #     return session


    def send_request(self, method, url, data, **kwargs):
        # 将字符串全部转化为小写lower
        method = str(method).lower()
        rep = None
        if method == 'get':
            #get的传参方式是 params
            rep = RequestsUnit.session.request(method, url=url, params=data, **kwargs)
        else:
            data = json.dumps(data)
            rep = RequestsUnit.session.request(method, url=url, data=data, **kwargs)
        return rep.text    #用文本格式的话, 框架兼容性会更好

    #统一请求进行封装
    def all_send_request(self, **kwargs):
        res = RequestsUnit.session.request(**kwargs)
        # print(**kwargs)
        return res
