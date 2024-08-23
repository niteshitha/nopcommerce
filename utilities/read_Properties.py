### This is the file, which we used to read the data from config.in file  ####

import configparser

config = configparser.RawConfigParser()   # Create one object to read the data from congig.ini
config.read(".\\Configurations\\config.ini")    # Created the path for reading

# Now we are fetching the values
# Create one class and for every value in config file create one static method in this class
class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info','admin_page_url')
        return url    # This will return - https://admin-demo.nopcommerce.com/login

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username    # This will return - admin@yourstore.com

    @staticmethod
    def get_password():
        pwd = config.get('admin login info', 'password')
        return pwd    # This will return - admin

    @staticmethod
    def get_invalid_username():
        invalid_Username = config.get('admin login info', 'invalid_username')
        return invalid_Username    # This will return - adminbad@yourstore.com


