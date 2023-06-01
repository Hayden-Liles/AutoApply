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
        self.wait = WebDriverWait(self.driver, 3)

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
        try:
            continueButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="continueButton"]')))
            self.actions.move_to_element(continueButton).click(continueButton).perform()
        except:
            apply_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="adventureButton"]')))
            self.actions.move_to_element(apply_button).click(apply_button).perform()
            formChoice = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="applyManually"]')))
            self.actions.move_to_element(formChoice).click(formChoice).perform()

        self.employedBeforeChoice()
        self.pickCountry('United States of America')
        self.fillName()
        self.fillAddress()
        self.fillPhone()
        time.sleep(.5)
        self.NextForm()
        time.sleep(10)


    # Select the radio button Been Employed Before
    def employedBeforeChoice(self):
        radio_button = self.wait.until(EC.presence_of_element_located((By.ID, '2')))
        radio_button.click()

    def pickCountry(self, country_name):
        dropdown_button = self.wait.until(EC.presence_of_element_located((By.ID, 'input-2')))
        dropdown_button.click()
        country_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[@role='option']/div[text()='{country_name}']")))
        country_option.click()

    def fillName(self):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-3')))
        if len(first_name_field.get_attribute('value')) == 0:
            first_name_field.send_keys('Hayden')
        last_name_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-4')))
        if len(last_name_field.get_attribute('value')) == 0:
            last_name_field.send_keys('Liles')

    def fillAddress(self):
        address_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-5')))
        if len(address_field.get_attribute('value')) == 0:
            address_field.send_keys('823 S Spoonbill Ave')
        city_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-6')))
        if len(city_field.get_attribute('value')) == 0:
            city_field.send_keys('Meridian')

        dropdown_button = self.wait.until(EC.presence_of_element_located((By.ID, 'input-7')))
        dropdown_button.click()
        time.sleep(.3)
        state_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[@role='option']/div[text()='Idaho']")))
        state_option.click()

        zip_code_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-8')))
        if len(zip_code_field.get_attribute('value')) == 0:
            zip_code_field.send_keys('83642')

    def fillPhone(self):
        phone_field = self.wait.until(EC.presence_of_element_located((By.ID, 'input-12')))
        if len(phone_field.get_attribute('value')) == 0:
            phone_field.send_keys('2085594366')

    def NextForm(self):
        continueButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-automation-id="bottom-navigation-next-button"]')))
        continueButton.click()
        time.sleep(1)

    def fillExperience(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-automation-id="jobTitle"]')))



browserController = BrowserController()
