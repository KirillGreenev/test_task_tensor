from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium import webdriver
import logging


class TestCase2:
    browser = BasePage(webdriver.Chrome(), 'https://sbis.ru/')
    locator = {
        'sbis_url': 'https://sbis.ru/',
        'contact_button': (By.CLASS_NAME, 'sbisru-Header__menu-item-1'),
        'change_region': (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'),
        'list_partners': (By.NAME, 'itemsContainer'),
        'Kamchatka_link': (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span'),
    }
    verification_data = {
        'home_region': 'Тюменская обл.',
        'Tyumen_partners': 'Тюмень',
        'slug_url': '41-kamchatskij-kraj',
        'browser_title': 'Камчатский',
        'Kamchatka_region': 'Камчатский край',
        'Kamchatka_partners': 'Петропавловск-Камчатский',
    }

    def test_home_region_check(self):
        self.browser.click_element(self.locator['contact_button'])
        change_region = self.browser.find_element(self.locator['change_region'])
        assert change_region.text == self.verification_data['home_region']
        logging.info('Домашний регион определился')
        assert self.verification_data['Tyumen_partners'] in self.browser.find_element(
            self.locator['list_partners']).text
        logging.info('Список партнёров для домашнего региона отобразился на сайте')
        self.browser.click_element(self.locator['change_region'])
        sleep(10)
        self.browser.click_element(self.locator['Kamchatka_link'])

    def test_Kamchatka_region_check(self):
        sleep(5)
        assert self.verification_data['slug_url'] in self.browser.get_current_url()
        logging.info('В url-адресе присутствует проверяемый slug')
        assert self.verification_data['browser_title'] in self.browser.get_title()
        logging.info('Заголовок страницы соответствует проверяемому')
        assert self.verification_data['Kamchatka_region'] == self.browser.find_element(
            self.locator['change_region']).text
        logging.info('Подставился выбранный регион')
        assert self.verification_data['Kamchatka_partners'] in self.browser.find_element(
            self.locator['list_partners']).text
        logging.info('Список партнёров для региона Камчатский край отобразился на сайте')
        self.browser.quit()
