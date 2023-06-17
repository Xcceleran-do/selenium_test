from selenium.webdriver.common.by import By
from colorama import Fore
import requests
import time

def check_broken_link(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "a")
    print("Checking ", len(links), " links (if there is broken link)")
    for link in links:
        url = link.get_attribute("href")
        if url != None:
            result = requests.head(url)

            if result.status_code != 200:
                print(Fore.RED+url, Fore.MAGENTA+str(result.status_code))