"""
Base Test Module
Contains common setup and teardown methods for all test scripts
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    """Base class with setup and teardown methods"""

    def __init__(self):
        self.driver = None
        self.wait = None

    def setup(self):
        """
        Setup method to initialize WebDriver
        Automatically manages ChromeDriver using webdriver-manager
        """
        print("Setting up Chrome WebDriver...")

        # Setup ChromeDriver automatically
        service = Service(ChromeDriverManager().install())

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=service)

        # Set implicit wait timeout (10 seconds)
        self.driver.implicitly_wait(10)

        # Set page load timeout (30 seconds)
        self.driver.set_page_load_timeout(30)

        # Setup explicit wait
        self.wait = WebDriverWait(self.driver, 15)

        print("Browser setup completed successfully\n")
        return self.driver

    def teardown(self):
        """
        Teardown method to close browser (Task 5)
        Ensures browser is closed after each test execution
        """
        if self.driver:
            self.driver.quit()
            print("\nBrowser closed successfully")
