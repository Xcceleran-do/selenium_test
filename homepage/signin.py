import time
from selenium.webdriver.common.by import By
import requests

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

def login_by_using_username_password(driver):
    
    username = "seleniumtesteruser"
    password = "WMdvK4WD*umYorUFsFtv"

    # Fill the username field
    username_field = driver.find_element(By.ID, "user_login")
    username_field.clear()
    username_field.send_keys(username)

    # Fill the password field
    password_field = driver.find_element(By.ID, "user_pass")
    password_field.clear()
    password_field.send_keys(password)

    print("Filled login fields successfully")
    # hcaptcha automation not implemented. solve it manually
    time.sleep(120)

    # Click the signin button
    signin_button = driver.find_element(By.ID, "wp-submit")
    signin_button.click()
    
    time.sleep(10)


def signin_test(driver):
    open_signin_modal(driver)
    # close_signin_modal(driver)
    login_by_using_username_password(driver)
