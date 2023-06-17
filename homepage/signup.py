import time
from selenium.webdriver.common.by import By

def open_signup_modal(driver):
    signupBtn = driver.find_element(By.ID, "signup")
    signupBtn.click()

    signupPopup = driver.find_element(By.ID, "signupModal")
    assert signupPopup.is_displayed()

    print("signup modal opened successfully")
    time.sleep(5)

def close_signup_modal(driver):

    signupcloseModal = driver.find_element(By.ID, "close-signup")
    signupcloseModal.click()
    is_closed = signupcloseModal.is_displayed()
    assert not is_closed

    print("signup modal closed successfully")
    time.sleep(2)

def signup_test(driver):
    open_signup_modal(driver)
    close_signup_modal(driver)