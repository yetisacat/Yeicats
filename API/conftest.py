import pytest

from API.testcases.login_test import get_token


#从 login_test 读取 token 过来,设置为全局变量
#使用 fixtrue 固件设置全局变量,此时传参为定义的函数名,global_token,才会生效.
#token 的作用域是在 function 函数上,而不是在 session 会话上.!!!!!!
@pytest.fixture(scope='function', autouse=True)
def global_token():
    global_token1 = get_token()
    return global_token1
