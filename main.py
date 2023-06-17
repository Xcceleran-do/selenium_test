from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

from homepage.open import *
from homepage.signup import *
from homepage.signin import *

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

open_homepage(driver)

signup_test(driver)
signin_test(driver)

# all tasks are completed
print("All tasks are completed")
time.sleep(10)
