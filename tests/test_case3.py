from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium import webdriver
import logging
import os


class TestCase3:
    driver = webdriver.Chrome
    locator = {
        'sbis_url': 'https://sbis.ru/',
        'download_SBIS': (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a'),
        'plugin_button': (By.XPATH, '//*[@name="TabButtons"]/div[2]/div[2]'),
        'download_link': (By.PARTIAL_LINK_TEXT, 'Скачать (Exe '),
        'download_dir': f'{os.getcwd()}\\download\\',
    }

    def test_file_size_comparison(self):
        browser = BasePage(self.driver(), self.locator['sbis_url'])
        browser.find_element(self.locator['download_SBIS']).send_keys(Keys.TAB)
        browser.click_element(self.locator['download_SBIS'])
        sleep(5)
        browser.click_element(self.locator['plugin_button'])
        download_text = browser.find_element(self.locator['download_link']).text.split()[-2]
        browser.click_element(self.locator['download_link'])
        sleep(15)
        file = os.listdir(self.locator['download_dir'])[-1]
        file_size = round(os.stat(f'{self.locator["download_dir"]}{file}').st_size / 1024 / 1024, 2)
        assert float(download_text) - 0.5 < file_size < float(download_text) + 0.5
        logging.info('Размер указанный на сайте совпадает с размером файла')
        browser.quit()