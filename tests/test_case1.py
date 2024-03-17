from time import sleep
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium import webdriver
import logging

class TestCase1:
    browser = BasePage(webdriver.Chrome(), 'https://sbis.ru/')
    locator = {
        'sbis_url': 'https://sbis.ru/',
        'contact_button': (By.CLASS_NAME, 'sbisru-Header__menu-item-1'),
        'tensor_banner': (By.CLASS_NAME, 'sbisru-Contacts__logo-tensor'),
        'cookie_close': (By.CLASS_NAME, 'tensor_ru-CookieAgreement__close'),
        'about': (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'),
        'image_1': (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img'),
        'image_2': (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img'),
        'image_3': (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img'),
        'image_4': (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img'),
        'block_search': (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'),
    }

    verification_data = {
        'tensor_url': 'https://tensor.ru/',
        'tensor_about_url': 'https://tensor.ru/about',
        'block_for_inspection': 'Сила в людях',
    }

    def test_check_tensor_url(self):
        self.browser.click_element(self.locator['contact_button'])
        # self.browser.find_element(*self.locator['tensor_banner']).click()
        self.browser.click_element(self.locator['tensor_banner'])
        self.browser.tabs()
        assert self.browser.get_current_url() == self.verification_data['tensor_url']
        logging.info('Открылась страница tensor.ru')

    def test_checking_for_block_existence(self):
        block = self.browser.find_element(self.locator['block_search']).text
        assert block == self.verification_data['block_for_inspection']
        logging.info('Есть блок "Сила в людях"')

    def test_check_url_about(self):
        self.browser.find_element(self.locator['cookie_close']).click()
        self.browser.click_element(self.locator['about'])
        sleep(5)
        assert self.browser.get_current_url() == self.verification_data['tensor_about_url']
        logging.info('Открылась страница tensor.ru/about')

    def test_checking_images_for_the_same_size(self):
        size_1 = self.browser.find_element(self.locator['image_1']).size
        size_2 = self.browser.find_element(self.locator['image_2']).size
        size_3 = self.browser.find_element(self.locator['image_3']).size
        size_4 = self.browser.find_element(self.locator['image_4']).size
        assert size_1 == size_2 == size_3 == size_4
        logging.info('У всех фотографий хронологии одинаковая высота и ширина')
        self.browser.quit()