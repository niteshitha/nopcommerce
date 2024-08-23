import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_Admin_Page import Login_Admin_Page
from utilities.read_Properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Add_Customer_Page import Add_Customer_Page

class Test_03_Add_New_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self,setup):
        self.logger.info("************ Test_03_Add_New_Customer Started****************")
        self.driver = setup     # Here we are calling the setup fixture, It will initiliazes/launch the browser
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)  #for "Login_Admin_Page" base class we created the object/page object(admin_loginpage)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.maximize_window()
        self.logger.info("*****************Login Completed*****************")
        self.logger.info("**********************************")
        self.logger.info("***************** Starting add customer list *****************")
        self.add_customer = Add_Customer_Page(self.driver)   # This is the object of add customer class
        self.add_customer.click_customers()
        self.add_customer.click_customers_from_menu_options()
        self.add_customer.click_addnew()
        self.logger.info("**********************************")
        self.logger.info("***************** Providing customer info started *****************")
        self.logger.info("**********************************")

        email = generate_random_email()

        self.add_customer.enter_email(email)
        self.add_customer.enter_password("Test@123")
        self.add_customer.enter_firstname("Jack")
        self.add_customer.enter_lastname("Shaw")
        self.add_customer.select_gender("Male")
        self.add_customer.enter_dob("05/05/1992")
        self.add_customer.enter_companyname("My_company")
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("Test store 2")
        self.logger.info("******************** Test store 2 Selected *******************")
        self.add_customer.select_customer_role("Guests")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.enter_admin_comments("Test admin comment")
        self.add_customer.click_save()
        time.sleep(4)
        # Test case validation as success message in body text
        customer_add_success_text = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH,"//div[@class='content-wrapper']/div[1]").text

        if customer_add_success_text in success_text:
            assert True
            self.logger.info("************** Test_03_Add_New_Customer test passed ***************")
            self.driver.close()
        else:
            self.logger.info("************** Test_03_Add_New_Customer test failed ***************")
            self.driver.save_screenshot(".\\screenshots\\test_add_new_customer.png")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits,k=8))  #8 characters username
    domain = random.choice(['gmail.com','yahoo.com','outlook.com','example.com']) # Choose
    return f'{username}@{domain}'


