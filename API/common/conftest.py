# setup/teardown 在每个用例之前和之后执行一次
# setup_class/teardown_class 在每个类之前和之后执行一次
# 部分前置:fixture 中 scope ="作用域", params ="数据驱动", autouse ="自动执行", ids ="自定义参数名", name ="重命名"
# 作用域可以是:function class  module"模块" package/session  可以用 yield 进行返回.
# 一般来说fixture 是和 conftext.py文件来一起使用的,用处是可以在多个 py 文件之间共享前置配置条件,
# 且 conftest.py里的方法可以直接使用,无须调用,conftest.py文件可以有多个,也可以有多个不同层级.
# 自动执行时,则是全局调用,,手动执行时,需要放在固定的函数方法里去调用


# 在请求之前清空 token 并重新写入.使用 fixtrue 固定装置在每次会话前进行清空
import pytest
from API.common.yaml_unit import clear_token_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_token():
    clear_token_yaml()
