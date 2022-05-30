import pytest
import os
import allure


class TestLogin:
    def test_login01(self):
        assert 1 + 1 == 2


if __name__ == '__main__':

    # 步骤1、--alluerdir 存放目录
    pytest.main(['test_func01.py', '-s', '--alluredir', '../report/tmp'])

    # 步骤2、allure generate allure报告  cmd命令
    # 将../report/tmp中的文件 生成报告放到 ../report/report
    os.system('allure generate ../report/tmp -o ../report/report --clean')