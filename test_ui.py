import pytest

from conftest import UiClient
import json


# def __init__(self, ini):
#    self = ini
# class initJson:
    # def __init__(self, m):
    #     self.name = m
    # with open('xPath.json') as f:
    #     temp = json.load(f)
    #
    # print(temp)
    #
    # for section, commands in temp.items():
    #     print(section)
    #     print('\n'.join(commands))

class TestSuite1(UiClient):
    @pytest.mark.parametrize("url", [
        "urlGoogle",
        "urlYande1x"
    ])
    def test_case1(self, url):
        UiClient.open_page_check_title(self, UiClient.tempJson(self, url))
        UiClient.assert_title(self, UiClient.tempJson(self, 'google'))
