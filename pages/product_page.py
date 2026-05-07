from selenium.webdriver.common.by import By


class ProductPage:

    NAME = (By.NAME, "name")
    SHORT_DESC = (By.NAME, "shortDescription")
    PRICE_NOTE = (By.NAME, "priceNote")
    BASE_PRICE = (By.NAME, "basePrice")
    BOND = (By.NAME, "bond")

    IMAGE_UPLOAD = (By.NAME, "inputFieldName")

    CATEGORY_DROPDOWN = (By.XPATH, "//button[contains(@class,'dropdown-toggle')]")

    CREATE_BTN = (By.XPATH, "//button[@type='submit' and normalize-space()='Create']")