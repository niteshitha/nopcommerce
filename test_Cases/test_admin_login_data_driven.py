import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_Admin_Page import Login_Admin_Page
from utilities.read_Properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()    # Calling static methods from read_Properties file
    logger = Log_Maker.log_gen()   # As we created this as static method so we are directly calling using class
    filePath = ".//test_Data//admin_login_data.xlsx"
    status_list=[]

    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("******************** test_valid_admin_login_data_driven started ******************")
        #self.driver = webdriver.Chrome()
        self.driver = setup    # Here we are implementing the fixture instead of above line
        self.driver.implicitly_wait(20)
        self.driver.get(self.admin_page_url)
        self.admin_loginpage = Login_Admin_Page(self.driver)   #for "Login_Admin_Page" base class we created the object/page object(admin_loginpage)

        # For getting row count function from excel_utils.py
        self.rows = excel_utils.get_row_count(self.filePath,"Sheet1")
        print("Number of rows :",self.rows)   # This is row count


        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.filePath,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.filePath, "Sheet1",r, 2)
            self.exp_Login = excel_utils.read_data(self.filePath, "Sheet1",r, 3)
            self.admin_loginpage.enter_username(self.username)
            self.admin_loginpage.enter_password(self.password)
            self.admin_loginpage.click_login()
            time.sleep(10)
            act_title = self.driver.title
            expec_title = "Dashboard / nopCommerce administration"

            #Now we are adding validations
            if act_title == expec_title:
                if self.exp_Login == 'Yes':
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")
                    self.admin_loginpage.click_logout()
                elif self.exp_Login == 'No':
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                    self.admin_loginpage.click_logout()
            elif act_title != expec_title:
                if self.exp_Login == "Yes":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_Login == "No":
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")

        print("Status list is",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is passed")
            assert True





