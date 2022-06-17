from Config.config import Testdata
from Pages.login_page import Login_page
from Tests.Test_base import BaseTest


class Test_Home(BaseTest):
    def test_homepage_title(self):
        self.loginpage = Login_page(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        title = homepage.get_home_page_title(Testdata.HOME_PAGE_TITLE)
        assert title == Testdata.HOME_PAGE_TITLE

    def test_homepage_header(self):
        self.loginpage = Login_page(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        header = homepage.get_header_value()
        assert header == Testdata.HOME_PAGE_HEADER

    def test_account_name(self):
        self.loginpage = Login_page(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        account_name = homepage.get_account_name_value()
        assert account_name == Testdata.ACCOUNT_NAME

    def test_settings_icon(self):
        self.loginpage = Login_page(self.driver)
        homepage = self.loginpage.do_login(Testdata.USERNAME, Testdata.PASSWORD)
        assert homepage.is_settings_icon_exists()
