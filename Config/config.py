from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Testdata:
    #CHROME_EXECUTABLE_PATH = webdriver.Chrome(ChromeDriverManager().install())
    # FIREFOX_EXECUTABLE_PATH = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    BASE_URL = 'https://app.hubspot.com/login'
    USERNAME = 'mayuri@simformsolutions.com'
    PASSWORD = 'Hotel_taj@123'

    LOGIN_PAGE_TITLE = 'HubSpot Login'
    HOME_PAGE_TITLE = 'User Guide | HubSpot'
    HOME_PAGE_HEADER = 'User Guide'
