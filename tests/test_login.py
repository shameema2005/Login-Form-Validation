import os, time, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

BASE = os.getenv("BASE_URL", "http://localhost:8085")
REMOTE = os.getenv("SELENIUM_URL")

class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        opts = Options()
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        cls.driver = (webdriver.Remote(command_executor=REMOTE, options=opts)
                      if REMOTE else webdriver.Chrome(options=opts))
        cls.driver.get(BASE)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(BASE)

    def login(self, user, password):
        self.driver.find_element(By.ID, "username").clear()
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def test_valid_login(self):
        self.login("student", "Student@123")
        self.assertIn("Login successful", self.driver.find_element(By.ID, "message").text)

    def test_empty_username(self):
        self.login("", "Student@123")
        self.assertIn("Username is required", self.driver.find_element(By.ID, "usernameError").text)

    def test_short_username(self):
        self.login("ab", "Student@123")
        self.assertIn("3–20", self.driver.find_element(By.ID, "usernameError").text)

    def test_short_password(self):
        self.login("student", "123")
        self.assertIn("at least 8", self.driver.find_element(By.ID, "passwordError").text)

    def test_wrong_credentials(self):
        self.login("student", "WrongPass123")
        self.assertIn("Invalid username", self.driver.find_element(By.ID, "message").text)

if __name__ == "__main__":
    unittest.main()
