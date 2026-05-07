import pytest
import allure

from modules.order_module import OrderModule
from utils.screenshot import take_screenshot


@pytest.mark.smoke
@allure.title("TC02 - Create Order Flow")
def test_create_order(driver):

    order = OrderModule(driver)

    with allure.step("Open Orders Page"):
        order.open_orders(
            "https://app-hire-x-dev-multi-tenant-angular-01-bkgee7ewapa0c5es.southeastasia-01.azurewebsites.net/supplier/orders"
        )

    with allure.step("Create Order Flow"):
        order.click_new_order()
        order.verify_create_form()
        order.select_random_customer()
        order.click_create()

    with allure.step("Add Product"):
        order.add_product("Set", 2)

    take_screenshot(driver, "order_completed")