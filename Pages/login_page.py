from selenium.webdriver.common.by import By

from Config.config import Testdata
from Pages.Base_page import BasePage
from Pages.homepage import HomePage


class Login_page(BasePage):
    '''By Locators - OR'''
    EMAIl = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    LOGIN_BUTTON = (By.ID,'loginBtn')
    SIGNUP_LINK = (By.LINK_TEXT,'Sign up')

    '''Constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.BASE_URL)
    '''page actions'''
    ''''use to get the page title'''
    def get_login_page_title(self,title):
        return self.get_title(title)

    '''use to check sign up link'''
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    '''use to login the app'''
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIl,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)



