from API.common.requests_unit import RequestsUnit


#使用 yaml_unit文件中,yaml 读取方法,将 token 取出来


class TestShuJu:
    # @pytest.mark.parametrize('caseinfo', YamlUtil().read_shuju_yaml('shuju_data.yaml'))
    def test_get_device_info(self, global_token):
        url = "https://hospital.zhenjingai.com/zhenjing-platform/deviceUsage/info/23002800"
        payload = {}
        headers = {
            'Authorization': global_token
        }
        device_info = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, data=payload)
        print(device_info.json())

        #如果没有打印出来设备编号的具体信息,则是跟账号权限相关

    def test_get_user_info(self, global_token):   #获取当前用户的信息
        url = "https://hospital.zhenjingai.com/zhenjing-platform/getInfo"
        payload = {}
        headers = {
            'Authorization': global_token
        }
        user_info = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, data=payload)
        print(user_info.json())

    def test_get_routers(self, global_token):
        url = "https://hospital.zhenjingai.com/zhenjing-platform/getRouters"
        payload = {}
        headers = {
            'Authorization': global_token
        }
        get_routers = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, data=payload)
        print(get_routers.json())
