import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_Admin_Page import Login_Admin_Page
from utilities.read_Properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()    # Calling static methods from read_Properties file
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()   # As we created this as static method so we are directly calling using class

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("******************** Test_01_Admin_Login ******************")
        self.logger.info("******************** Verification of admin login page title ******************")

        #self.driver = webdriver.Chrome()  #By this we can able to access the class variables(admin_page_url,username,password,invalid_username)
        self.driver = setup    # Here we are implementing the fixture instead of above line
        self.driver.get(self.admin_page_url)
        actual_Title = self.driver.title
        expec_Title = "Your store. Login"
        if actual_Title == expec_Title:
            self.logger.info("******************** test_title_verification title matched ******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_title_verification.png")
            self.logger.info("******************** test_title_verification title not matched ******************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("******************** test_valid_admin_login started ******************")
        #self.driver = webdriver.Chrome()
        self.driver = setup    # Here we are implementing the fixture instead of above line
        self.driver.get(self.admin_page_url)
        self.admin_loginpage = Login_Admin_Page(self.driver)   #for "Login_Admin_Page" base class we created the object/page object(admin_loginpage)
        self.admin_loginpage.enter_username(self.username)
        self.admin_loginpage.enter_password(self.password)
        self.admin_loginpage.click_login()
        actual_dashboardText = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if actual_dashboardText == "Dashboard":
            self.logger.info("******************** Dashboard text found ******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("******************** test_invalid_admin_login started ******************")
        #self.driver = webdriver.Chrome()
        self.driver = setup  # Here we are implementing the fixture instead of above line
        self.driver.get(self.admin_page_url)
        self.admin_loginpage = Login_Admin_Page(self.driver)   #for "Login_Admin_Page" base class we created the object/page object(admin_loginpage)
        self.admin_loginpage.enter_username(self.invalid_username)
        self.admin_loginpage.enter_password(self.password)
        self.admin_loginpage.click_login()
        Err_Msg = self.driver.find_element(By.XPATH,"//li").text
        if Err_Msg == "No customer account found":
            self.logger.info("******************** test_invalid_admin_login error messages matched ******************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False
