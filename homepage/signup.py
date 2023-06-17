import time
from selenium.webdriver.common.by import By

def open_signup_modal(driver):
    button1 = driver.find_element(By.ID, "signup")
    button1.click()

    popup1 = driver.find_element(By.ID, "signupModal")
    assert popup1.is_displayed()

    print("signup modal opened successfully")
    time.sleep(5)

def close_signup_modal(driver):

    closeModal1 = driver.find_element(By.ID, "close-signup")
    closeModal1.click()
    is_closed = closeModal1.is_displayed()
    assert not is_closed

    print("signup modal closed successfully")
    time.sleep(2)
