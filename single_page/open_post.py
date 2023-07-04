import time
from selenium.webdriver.common.by import By

def open_single_post(driver):
    driver.implicitly_wait(10)
    post_link = driver.find_element(By.CLASS_NAME, 'hero-href')
    
    #click to open post
    post_link.click()
    print('post opened successfully')
    
    time.sleep(10)