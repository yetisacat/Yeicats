import os
import pytest

if __name__ == '__main__':
    pytest.main()
    #执行系统命令,用来生成 allure 报告
    # os.system("allure generate ./temp -o ./reports  --clean")
