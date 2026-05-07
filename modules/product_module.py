import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.product_page import ProductPage
from utils.image_provider import ImageProvider


class ProductModule:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)  # 🔥 increased wait
        self.page = ProductPage()
        self.image_provider = ImageProvider()

    def enter_text(self, locator, value):

        field = self.wait.until(
            EC.element_to_be_clickable(locator)   # 🔥 better than visibility
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", field)
        field.clear()
        field.send_keys(value)

    def upload_image(self):

        with allure.step("Upload Product Image"):

            image_file = self.image_provider.get_next_image_file()

            file_input = self.wait.until(
                EC.presence_of_element_located(self.page.IMAGE_UPLOAD)
            )

            file_input.send_keys(image_file)

            return image_file

    def create_product(self, name, desc, price, bond):

        with allure.step("Fill Product Form"):

            self.enter_text(self.page.NAME, name)
            self.enter_text(self.page.SHORT_DESC, desc)
            self.enter_text(self.page.BASE_PRICE, price)
            self.enter_text(self.page.BOND, bond)

        self.upload_image()

        with allure.step("Click Create Button"):

            btn = self.wait.until(
                EC.element_to_be_clickable(self.page.CREATE_BTN)
            )

            self.driver.execute_script("arguments[0].click();", btn)

            time.sleep(2)