import json

import allure
import pytest
import requests
from allure_commons.types import AttachmentType


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)


from selenium import webdriver

exec_path = 'C:/chromedriver/chromedriver.exe'


class UiClient:
    # def __init__(self, element):
    #     self.element = element

    def tempJson(self, name):
        with open('xPath.json') as f:
            temp = json.load(f)
            return temp[name]

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()


    def find_element(self, element):
        find = self.driver.find_element_by_xpath(element)
        find = self.driver.find_element_by_id(element)
        find = self.driver.find_element_by_link_text(element)
        find = self.driver.find_element_by_partial_link_text(element)
        find = self.driver.find_element_by_name(element)
        find = self.driver.find_element_by_tag_name(element)
        find = self.driver.find_element_by_class_name(element)
        find = self.driver.find_element_by_css_selector(element)


    @allure.feature('open page')
    @allure.story('Открываем страницу google')
    @allure.severity('normal')
    def open_page_check_title(self, name):
        self.driver.get(name)
        with allure.step('Скрин'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    @allure.feature('assert Title')
    @allure.story('Проверяем Тайтл страницы')
    def assert_title(self, title):
        assert self.driver.title == title

    @allure.feature('get text')
    @allure.story('Получаем текст элемента')
    def get_text(self, name):
        element = self.driver.find_element_by_xpath(name).get_attribute('value')
        if element is None:
            element = self.driver.find_element_by_xpath(name).text
        return element
    # @allure.feature('open pagei1')
    # @allure.story('Открываем страницу google')
    # def test_yandex_search(self):
    #     self.driver.get('https://yandex.ru')
    #     assert self.driver.title == 'Яндекс'
