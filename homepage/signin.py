import time
from selenium.webdriver.common.by import By

def open_signin_modal(driver):
    signinBtn = driver.find_element(By.ID, "signin")
    signinBtn.click()

    signinPopup = driver.find_element(By.ID, "signinModal")
    assert signinPopup.is_displayed()

    print("signin modal opened successfully")
    time.sleep(5)

def close_signin_modal(driver):

    closeSigninModal = driver.find_element(By.ID, "close-signin")
    closeSigninModal.click()
    is_closed = closeSigninModal.is_displayed()
    assert not is_closed

    print("signin modal closed successfully")
    time.sleep(2)

def signin_test(driver):
    open_signin_modal(driver)
    close_signin_modal(driver)