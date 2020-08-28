from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import platform

class Browser(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        if platform.system().lower() == 'windows':
            super().__init__(ChromeDriverManager().install(),options=chrome_options)
        else:
            super().__init__(options=chrome_options)
    
    def wait_element_by_css_selector(self,css_selector,delay=300):
        try:
            element = WebDriverWait(self, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
            return element
        except TimeoutException:
            raise Exception(f'Page did not found your element in {delay} seconds')