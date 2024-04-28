import json
from API.common.requests_unit import RequestsUnit


class TestPatient:
    # session 是 requests 里自带的方法,建立统一会话,且在每个执行方法中调用统一会话,调用的时候不要忘记()
    # session = requests.session()     #写法二:设置为全局的类变量
    # def get_seesion(self):      #写法一,这样写的话,每调用一次,session 会重新生成一次.接口可能会有失败的风险.
    #     session = requests.session()
    #     return session

    def test_patient_info(self, global_token):
        url = "https://hospital.zhenjingai.com/zhenjing-platform/patients/list"  # 把 list 后面的入参写在 data 里
        data = {
            'pageNum': 1,
            'pageSize': 5,
            'delFlag': 0,
            'orderByColumn': id,
            'isAsc': 'desc'
        }
        headers = {
            'Authorization': global_token
        }
        # 方法一: 使用当前文件的封装 self.get_seesion().request 这个是调用统一会话方式
        # patient_info = TestPatient.session.request(method="GET", url=url, headers=headers, data=data)
        patient_info = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, data=data)
        print(patient_info.json())

    # 方法二:使用全局封装,导入全局封装的请求单元 requests_unit中,但是全局封装是返回是 text 格式,可以使用 json.loads 转成 json 格式
    # patient = RequestsUnit.session.request(method, url, data, headers)
    # print(patient)

    def test_search_patient(self, global_token):
        url = "https://hospital.zhenjingai.com/zhenjing-platform/patients/list"
        payload = {
            'pageNum': 1,
            'pageSize': 10,
            'name': "周",
            'idNo': '3',
            'sex': 1,
            'phoneNumber': '',
            'orderByColumn': 'id',
            'isAsc': 'desc',
            'organizationName': ''
        }
        headers = {
            'Authorization': global_token
        }
        search_patient = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, params=payload)
        print(search_patient.json())

    def test_modify_patient_info(self, global_token):
        url = "https://hospital.zhenjingai.com/zhenjing-platform/patients"
        data = json.dumps({
            "id": 749,
            "name": "python111"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': global_token
        }
        modify_info = RequestsUnit().all_send_request(method="PUT", url=url, headers=headers, data=data)
        print(modify_info.json())


#   新建患者信息,一般不使用.
    # def test_create_new_patient(self):
    #     url = "https://hospital.zhenjingai.com/zhenjing-platform/patients"
    #     params = json.dumps({
    #         "birthAddressList": [       # 出生地
    #             "山西省",
    #             "阳泉市",
    #             "矿区"
    #         ],
    #         "permanentlyAddressList": [      # 常住地
    #             "河北省",
    #             "秦皇岛市",
    #             "海港区"
    #         ],
    #         "name": "32111",             # 必填
    #         "birthday": "1993-11-12",    # 必填
    #         "sex": "1",                  # 必填
    #         "hisNum": "",                # 机构档案编号
    #         "idNo": "",                  # 身份证号
    #         # "phoneNumber": "",         #前端非必填, 后端必填.
    #         "occupation": "2",           # 职业
    #         "maritalStatus": "0",        # 婚姻状态，0未婚，1已婚
    #         "birthProvince": "山西省",
    #         "birthCity": "阳泉市",
    #         "birthDistrict": "矿区",
    #         "permanentlyProvince": "河北省",
    #         "permanentlyCity": "秦皇岛市",
    #         "permanentlyDistrict": "海港区",
    #         "params": {
    #             "sameName": 'false'
    #         }
    #     })
    #     headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': token_set
    #     }
    #     create = RequestsUnit().all_send_request(method="POST", url=url, headers=headers, data=params)
    #     print(create.json())


