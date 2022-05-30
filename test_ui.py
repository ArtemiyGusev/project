import allure
from allure_commons.types import AttachmentType

from selenium import webdriver

exec_path = 'C:/chromedriver/chromedriver.exe'


class TestPage1:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()

    @allure.feature('open page')
    @allure.story('Открываем страницу google')
    @allure.severity('normal')
    def test_google_search(self):
        self.driver.get('https://google.com')
        with allure.step('Скрин'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('open pagei')
    @allure.story('Открываем страницу google6')
    def test_yandex_search(self):
        self.driver.get('https://yandex.ru')
        assert self.driver.title == 'Яндекс'
