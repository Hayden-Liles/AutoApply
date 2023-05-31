from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class BrowserController:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bah.wd1.myworkdayjobs.com/en-US/BAH_Jobs/login')
        wait = WebDriverWait(self.driver, 50)
        email_element = wait.until(EC.presence_of_element_located((By.ID, 'input-4')))
        email_element.send_keys('lileshaydenreal@gmail.com')
        password_element = wait.until(EC.presence_of_element_located((By.ID, 'input-5')))
        password_element.send_keys('Sanderman1!')
        signin_div = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-automation-id="click_filter"]')))
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_div).click(signin_div).perform()
        time.sleep(6)
        self.driver.quit()

browserController = BrowserController()
