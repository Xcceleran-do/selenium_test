from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options

from homepage.open import *
from search_page.search import search_test
from homepage.signup import *
from homepage.signin import *
from shared.broken_link_check import *
from single_page.open_post import *
from single_page.interact import *
from menu_icon.test_menu_icon import *

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

open_homepage(driver)
# check_broken_link(driver)

# signup_test(driver)

signin_test(driver) # hcaptcha automation not implemented. solve it manually!
# check_broken_link(driver)

# tasks after signed in will be procced blow
test_sidebar_open(driver)
#open_single_post(driver)
#interaction_test(driver)

# the search test below can be executed without signing in.
# one can comment out the signIn test above and only test for the search functionality.
# search_test(driver)





# all tasks are completed
print("All tasks are completed")
time.sleep(10)
