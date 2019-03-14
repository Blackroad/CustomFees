from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "InternetExplorer":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.config = config
        self.base_url = config["web"]["baseURL"]

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        self.login()

    def login(self):
        wd = self.wd
        self.wait("//div[@class='login_panel']")
        wd.find_element_by_id('usernameField').send_keys(self.config["user"]["login"])
        wd.find_element_by_id('passwordField').send_keys(self.config["user"]["pass"])
        wd.find_element_by_xpath("//button[@onclick ='submitCredentials()']").click()

    def open_time_card_creator(self):
        wd = self.wd
        self.wait("//ul[@id='treemenu1']")
        wd.find_element_by_xpath("//ul[@id='treemenu1']").click()
        wd.find_element_by_xpath("//ul[@id='treemenu1']//li//div[text()='Timesheet']").click()
        wd.find_element_by_xpath("//ul//li[@id='LITimesheetRecent_Timecards']").click()

    def get_date_values(self):
        wd = self.wd
        get_id = [i.text for i in (wd.find_elements_by_xpath("//tr[6]//tbody//th")[3:-3])]

    def wait(self, element):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, element)))

    def destroy(self):
        self.wd.quit()
