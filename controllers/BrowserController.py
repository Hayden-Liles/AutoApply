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
        self.wait = WebDriverWait(self.driver, 10)
        self.wait3 = WebDriverWait(self.driver, 3)
        self.MyExperience = [
            dict(
            title = 'Full Stack Developer (Freelance)',
            company = 'Bice Ltd',
            location = 'Remote',
            curWork = True,
            dateFromMonth = '04',
            dateFromYear = '2023',
            dateToMonth = '00',
            dateToYear = '0000',
            description = """Integrated various APIs such as LinkedIn and Twitter, leveraging web scraping techniques to gather valuable data for clientele
Devised and implemented efficient scripts that streamlined client-business communications.
Leveraged extensive knowledge of WordPress databases to create innovative scripts, which expedited the post creation process, improving overall efficiency and productivity.
Leveraged knowledge of full-stack technologies to create responsive and intuitive user interfaces, while ensuring optimal performance on the back-end, thereby elevating the overall web development process."""
            ),
            dict(
            title = 'Team Lead Canvasser',
            company = 'Dabella Exteriors',
            location = 'Boise Idaho',
            curWork = False,
            dateFromMonth = '01',
            dateFromYear = '2021',
            dateToMonth = '11',
            dateToYear = '2022',
            description = """Managed and mentored a team of 5, providing daily guidance to help them achieve their goals and grow professionally
Served as the primary trainer for new canvassers, equipping them with the skills to excel in their roles
Generated over 250 leads, resulting in $1.3 million in revenue within the first year"""
            ),
            dict(
            title = 'Apprentice Carpenter',
            company = 'Curtis Construction',
            location = 'Meridian Idaho',
            curWork = False,
            dateFromMonth = '06',
            dateFromYear = '2019',
            dateToMonth = '01',
            dateToYear = '2021',
            description = """Assisted in various aspects of home remodeling, including roofing, interior renovations, and plumbing
Collaborated with clients to understand their needs and ensure timely, high-quality project completion
Demonstrated strong time management and communication skills"""
            ),
            dict(
            title = 'Caregiver',
            company = 'Living Resources of Idaho',
            location = 'Meridian Idaho',
            curWork = False,
            dateFromMonth = '08',
            dateFromYear = '2018',
            dateToMonth = '06',
            dateToYear = '2019',
            description = """Provided comprehensive care for adults with mental disabilities, ensuring their needs were met throughout the day
Practiced effective time management to maintain a consistent schedule and support clients in their daily activities"""
            ),
        ]
        self.myEducation = [dict(
            title = 'Boise CodeWorks',
            degree = 'Other'
        )]
        self.myLanguages = [dict(
            language = 'English',
            fluent = True,
            Overall = '5 - Complete Mastery'
        ),dict(
            language = 'English',
            fluent = True,
            Overall = '5 - Complete Mastery'
        ),]
    
    
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
            continueButton = self.wait3.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="continueButton"]')))
            self.actions.move_to_element(continueButton).click(continueButton).perform()
        except:
            apply_button = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="adventureButton"]')))
            self.actions.move_to_element(apply_button).click(apply_button).perform()
            formChoice = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-automation-id="applyManually"]')))
            self.actions.move_to_element(formChoice).click(formChoice).perform()


        time.sleep(3)
        self.employedBeforeChoice()
        self.pickCountry('United States of America')
        self.fillName()
        self.fillAddress()
        self.fillPhone()
        self.NextForm()
        time.sleep(2)
        self.fillExperience()
        self.fillEducation()
        self.fillLanguages()
        time.sleep(30)


    # Select the radio button Been Employed Before
    def employedBeforeChoice(self):
        radio_button = self.wait.until(EC.presence_of_element_located((By.ID, '2')))
        radio_button.click()

    def pickCountry(self, country_name):
        dropdown_button = self.wait.until(EC.presence_of_element_located((By.ID, 'input-2')))
        dropdown_button.click()
        time.sleep(.5)
        country_option = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//li[@role='option']/div[text()='{country_name}']")))
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
        self.driver.execute_script("arguments[0].scrollIntoView();", dropdown_button)
        time.sleep(0.5)  # just in case we need a little extra time for scrolling
        self.driver.execute_script("arguments[0].click();", dropdown_button)

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
        job_title_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="jobTitle"]')
        if len(job_title_elements) != len(self.MyExperience):
            experienceDiffrenceNum = (len(self.MyExperience) - len(job_title_elements))
            for x in range(experienceDiffrenceNum):
                addAnotherExperienceButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add Another Work Experience"]')))
                self.driver.execute_script("arguments[0].click();", addAnotherExperienceButton)
        time.sleep(.5)
        # NOTE filling out experience job titles
        job_title_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="jobTitle"]')
        for index, title in enumerate(job_title_elements):
            res = self.MyExperience[index]['title']
            title.send_keys(res)
        # NOTE filling out experience job companies
        job_company_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="company"]')
        for index, company in enumerate(job_company_elements):
            res = self.MyExperience[index]['company']
            company.send_keys(res)
        # NOTE filling out experience job locations
        job_location_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="location"]')
        for index, location in enumerate(job_location_elements):
            res = self.MyExperience[index]['location']
            location.send_keys(res)

        month_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="dateSectionMonth-input"]')
        for index in range(0, len(month_elements), 2):
            theMonthInput = month_elements[index]
            theMonthInput.send_keys((self.MyExperience[index//2]['dateFromMonth'] + self.MyExperience[index//2]['dateFromYear']))
        for index in range(1, len(month_elements), 2):
            theMonthInput = month_elements[index]
            theMonthInput.send_keys((self.MyExperience[index//2]['dateToMonth'] + self.MyExperience[index//2]['dateToYear']))

        # NOTE Selecting the radio button for if they currently work at this place
        job_curWork_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="currentlyWorkHere"]')
        for index, curWorkButton in enumerate(job_curWork_elements):
            res = self.MyExperience[index]['curWork']
            if res == True:
                self.driver.execute_script("arguments[0].click();", curWorkButton)

        job_description_elements = self.driver.find_elements(By.XPATH, '//textarea[@data-automation-id="description"]')
        for index, description in enumerate(job_description_elements):
            res = self.MyExperience[index]['description']
            description.send_keys(res)
    
    def fillEducation(self):
        school_title_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="school"]')
        if len(school_title_elements) != len(self.myEducation):
            educationDifferenceNum = (len(self.myEducation) - len(school_title_elements))
            for x in range(educationDifferenceNum):
                addAnotherEducationButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add Another Education"]')))
                self.driver.execute_script("arguments[0].click();", addAnotherEducationButton)
        time.sleep(.5)

        school_name_elements = self.driver.find_elements(By.XPATH, '//input[@data-automation-id="school"]')
        for index, title in enumerate(school_name_elements):
            res = self.myEducation[index]['title']
            title.send_keys(res)

        degree_dropdown_elements = self.driver.find_elements(By.XPATH, '//button[@aria-label="Degree select one required"]')
        for index, dropdown in enumerate(degree_dropdown_elements):
            res = self.myEducation[index]['degree']
            dropdown.click()
            time.sleep(.5)
            degree_option = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//li[@role='option']/div[text()='{res}']")))
            degree_option.click()


    def fillLanguages(self):
        try:
            languagesAddButton = self.driver.find_element(By.XPATH, '//button[@aria-label="Add Languages"]')
            languagesAddButton.click()
        except:
            pass

        try:
            languageDropdownList = self.wait.until(EC.presence_of_all_elements_located(((By.XPATH, '//button[@aria-label="Language select one required"]'))))

            if len(languageDropdownList) != len(self.myLanguages):
                languageDifferenceNumber = (len(self.myLanguages) - len(languageDropdownList))
                for x in range(languageDifferenceNumber):
                    addAnotherLanguageButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Add Another Languages"]')))
                    self.driver.execute_script("arguments[0].click();", addAnotherLanguageButton)
            time.sleep(.5)
            languageDropdownList = self.wait.until(EC.presence_of_all_elements_located(((By.XPATH, '//button[@aria-label="Language select one required"]'))))
        except:
            pass

    



browserController = BrowserController()
