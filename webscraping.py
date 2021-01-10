from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

class Tinder:
    def __init__(self, timeout=10):
        '''
        inits Tinder object
        param timeout means the maximum time the bot will wait for buttons
        :param timeout: int
        :return: Tinder
        '''
        self.url = 'https://tinder.com/app/recs'
        self.timeout = timeout
        self.driver = webdriver.Chrome('../../chromedriver.exe')
        self.driver.get(self.url)

    def login(self, number):
        '''
        puts phone number on login and waits for manual verification
        :param number: str
        :return: (name: str, description: str)
        '''

        loginButtonPath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable((By.XPATH, loginButtonPath)))
        loginButton = self.driver.find_element_by_xpath(loginButtonPath)
        loginButton.click()
        
        loginPhoneButtonPath = '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button'
        wait.until(EC.presence_of_element_located((By.XPATH, loginPhoneButtonPath)))
        loginPhoneButton = self.driver.find_element_by_xpath(loginPhoneButtonPath)
        loginPhoneButton.click()

        phoneInputPath = '//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input'
        wait.until(EC.presence_of_element_located((By.XPATH, phoneInputPath)))
        phoneInput = self.driver.find_element_by_xpath(phoneInputPath)
        phoneInput.send_keys(number)

        input('press enter after checking your account')

    def accept_person(self):
        '''
        tries to click accept button
        :return: None
        '''

        acceptButtonPath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        acceptButton = self.driver.find_element_by_xpath(acceptButtonPath)
        
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable((By.XPATH, acceptButtonPath)))

        while True:
            try:
                acceptButton.click()
                break
            except ElementClickInterceptedException:
                wait.until(EC.element_to_be_clickable((By.XPATH, acceptButtonPath)))

    def reject_person(self):
        '''
        tries to click reject button
        :return: None
        '''
        
        rejectButtonPath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button'
        rejectButton = self.driver.find_element_by_xpath(rejectButtonPath)
        
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable((By.XPATH, rejectButtonPath)))

        try:
            rejectButton.click()
        except ElementClickInterceptedException:
            wait.until(EC.element_to_be_clickable((By.XPATH, rejectButtonPath)))        

    def get_person_data(self):
        '''
        returns the persons name and description
        :return: (name: str, description: str)
        '''

        namePath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/div/span'
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, namePath)))
        
        name = self.driver.find_element_by_xpath(namePath).get_attribute('innerHTML')
        descriptionPath = '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[2]/div/div[2]'
        try:
            description = self.driver.find_element_by_xpath(descriptionPath).get_attribute('innerHTML')
        except:
            description = -1
        return (name, description)

    def close(self):
        self.driver.close()
