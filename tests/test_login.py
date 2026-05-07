import pytest
import allure
from utils.screenshot import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
@allure.title("TC01 - Verify Dashboard Load after Login")
def test_login_grandrest(driver):

    wait = WebDriverWait(driver, 20)

    with allure.step("Verify user is on dashboard"):
        try:
            wait.until(EC.url_contains("/supplier/dashboard"))
            take_screenshot(driver, "dashboard_success")
        except:
            take_screenshot(driver, "dashboard_failed")
            pytest.fail("Dashboard not loaded")