from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    EMAIL = (By.XPATH, "//input[contains(@type,'email')]")
    PASSWORD = (By.XPATH, "//input[contains(@type,'password')]")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(),'Login')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, email, password):
        email_input = self.wait.until(EC.visibility_of_element_located(self.EMAIL))
        password_input = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))

        email_input.send_keys(email)
        password_input.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()