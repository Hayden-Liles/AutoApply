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
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 50)

    def login(self):
        self.driver.get('https://bah.wd1.myworkdayjobs.com/en-US/BAH_Jobs/login')
        email_element = self.wait.until(EC.presence_of_element_located((By.ID, 'input-4')))
        email_element.send_keys('lileshaydenreal@gmail.com')
        password_element = self.wait.until(EC.presence_of_element_located((By.ID, 'input-5')))
        password_element.send_keys('Sanderman1!')
        signin_div = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-automation-id="click_filter"]')))
        self.actions.move_to_element(signin_div).click(signin_div).perform()
        time.sleep(1)
        self.fillForm('https://bah.wd1.myworkdayjobs.com/BAH_Jobs/job/Annapolis-Junction-MD/Software-Developer_R0128931-1?source=JB-16500')

    def fillForm(self, formLink):
        self.driver.get(formLink)
        apply_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="adventureButton"]')))
        self.actions.move_to_element(apply_button).click(apply_button).perform()
        formChoice = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="applyManually"]')))
        self.actions.move_to_element(formChoice).click(formChoice).perform()

        # Select the radio button
        radio_button = self.wait.until(EC.presence_of_element_located((By.ID, '2')))
        radio_button.click()
        self.pickCountry('United States of America')

    def pickCountry(self, country_name):
        dropdown_button = self.wait.until(EC.presence_of_element_located((By.ID, 'input-2')))
        dropdown_button.click()
        self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'li')))

        options = self.driver.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if option.text == country_name:
                # self.driver.execute_script("arguments[0].scrollIntoView();", option)
                option.click()
                break
        time.sleep(10)

browserController = BrowserController()
