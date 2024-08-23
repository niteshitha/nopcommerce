from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options,service=ChromeService())

########################### This is creation of page object ############
#class with class name
class Login_Admin_Page:
    #textbox_username_id = "Email"   # Here this is textbox and it is username and we are taking id attribute
    textbox_username_xpath = "//input[@id='Email']"
    #textbox_password_id = "Password" # Here this is textbox and it is password and we are taking id attribute
    textbox_password_xpath = "//input[@id='Password']"
    btn_login_xpath = "//button[@type='submit']" # This is the login button and choosing XPath
    logout_linktext = "Logout"     #Choosing linktext

    # Write one constructor, one parameter named-'driver',This will access the above class variables(Login_Admin_Page)
    def __init__(self,driver):
        self.driver = driver

    #Now writing the action methods for this page
    def enter_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()







