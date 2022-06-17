import pytest
from Config.config import Testdata
from Pages.login_page import Login_page
from Tests.Test_base import BaseTest


class Test_login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = Login_page(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage=Login_page(self.driver)
        title=self.loginPage.get_title(Testdata.LOGIN_PAGE_TITLE)
        assert title == Testdata.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = Login_page(self.driver)
        self.loginPage.do_login(Testdata.USERNAME,Testdata.PASSWORD)


