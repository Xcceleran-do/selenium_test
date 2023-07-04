import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # for pressing the enter key
    

def go_to_search_page(driver):
    # let's click on the search button
    search_button = driver.find_element(By.XPATH, "//a[@href='https://staging.mindplex.ai/search']")
    assert search_button.is_displayed(), "search button is not displayed."
    search_button.click()
    # let's wait for the title of the page to `match the expected title of the search page.
    # this is how we know the search page has opened.
    WebDriverWait(driver, 15).until(EC.title_is("search - Mindplex_iCog"), f"Search page could not be loaded in 15 seconds.",)
    print("Search page loaded successfully.")

def search_by_keyword(driver):
    # let's search by keyword
    search_input = driver.find_element(By.XPATH, "//input[@type='text' and @class='trips-search']")
    assert search_input.is_displayed(), "could not find the search input."
    print("Search input found.")

    # now let's enter some keys into the search field to make sure users can enter text into the search field.
    search_input.send_keys("test")
    entered_text = search_input.get_attribute("value")
    assert entered_text == "test", "could not enter text into the search field."
    print("Text entered into the search field successfully.")

    # now let's submit the search form by pressing the enter key and see if the search works.
    search_input.send_keys(Keys.ENTER)
    # let's see if the heading of the search page contains the keyword we searched for.
    # this is how we know the search worked (at least for now)
    search_heading = driver.find_element(By.XPATH, "//h1[@class='search-content-indicator']")
    assert search_heading.is_displayed(), "could not find the heading of the search page."
    assert search_heading.text.lower().find("test") != -1, "Search likely did not work. " \
        "Heading of the search page does not contain the keyword we searched for."
    print("Search by pressing enter key worked successfully.")
    time.sleep(2)
    
    # now let's click on the search button to perform a search
    search_button = driver.find_element(By.XPATH, "//input[@type='button' and @class='trip-search-btn' and @value='search']")
    assert search_button.is_displayed(), "could not find the search button."
    search_input = driver.find_element(By.XPATH, "//input[@type='text' and @class='trips-search']")
    search_input.clear()
    search_input.send_keys("mindplex")
    search_button.click()
    time.sleep(6)

    # let's see if the heading of the search page contains the keyword we searched for.
    # this is how we know the search worked (at least for now)
    search_heading = driver.find_element(By.XPATH, "//h1[@class='search-content-indicator']")
    assert search_heading.is_displayed(), "could not find the heading of the search page."
    assert search_heading.text.lower().find("mindplex") != -1, \
    "Search likely did not work by clicking on the search button. " \
    "Heading of the search page does not contain the keyword we searched for."
    print("Search by clicking on the search button worked successfully.")
    time.sleep(3)

def search_test(driver):
    go_to_search_page(driver)
    search_by_keyword(driver)

