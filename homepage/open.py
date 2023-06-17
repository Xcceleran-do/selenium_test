import time

def open_homepage(driver):
    driver.get("https://staging.mindplex.ai/")

    time.sleep(6)

    # button2 = driver.find_element(By.ID, "signin")
    # time.sleep(15)
    # button2.click()

    # popup2 = driver.find_element(By.ID, "signinModal")
    # assert popup2.is_displayed()
    # time.sleep(5)

    # closeModal2 = driver.find_element(By.ID, "close-signin")
    # closeModal2.click()
    # is_closed = closeModal2.is_displayed()
    # assert not is_closed
