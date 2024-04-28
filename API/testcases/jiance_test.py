# 检测记录
from API.common.requests_unit import RequestsUnit


class TestDetection:

    def test_records(self, global_token):
        url = 'https://hospital.zhenjingai.com/zhenjing-platform/examination/record/list'
        data = {
            'pageNum': 1,
            'pageSize': 10
        }
        headers = {
            'Authorization': global_token
        }
        records = RequestsUnit().all_send_request(method="GET", url=url, headers=headers, data=data)
        print(records.json())


