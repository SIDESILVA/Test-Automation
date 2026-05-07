import os
import allure

def take_screenshot(driver, step_name):
    os.makedirs("reports", exist_ok=True)
    path = f"reports/{step_name}.png"
    driver.save_screenshot(path)

    allure.attach.file(
        path,
        name=step_name,
        attachment_type=allure.attachment_type.PNG
    )