from selenium.webdriver.common.by import By


class TaskPage:

    # Buttons
    NEW_BUTTON = (
        By.XPATH,
        "//button[text()='New']"
    )

    CREATE_BUTTON = (
        By.XPATH,
        "//button[text()='Create']"
    )

    # Dropdowns
    TASK_TYPE_DROPDOWN = (
        By.NAME,
        "noteTypeId"
    )

    TASK_TYPE_OPTIONS = (
        By.XPATH,
        "//select[@name='noteTypeId']/option"
    )

    USER_DROPDOWN = (
        By.NAME,
        "user"
    )

    USER_OPTIONS = (
        By.XPATH,
        "//select[@name='user']/option"
    )

    # Loading
    SPINNER = (
        By.CLASS_NAME,
        "spinner-wrapper"
    )