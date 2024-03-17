from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, web_driver, url='', timeout=10):
        self._web_driver = web_driver
        self.get(url, timeout)

    def get(self, url, timeout=10):
        self._web_driver.get(url)
        self._wait_for_page_load(timeout)

    def _wait_for_page_load(self, timeout):
        wait = WebDriverWait(self._web_driver, timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

    def get_current_url(self):
        return self._web_driver.current_url

    def get_title(self):
        return self._web_driver.title

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self._web_driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self._web_driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def tabs(self):
        self._web_driver.switch_to.window(self._web_driver.window_handles[-1])

    def quit(self):
        self._web_driver.quit()
