from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def is_sidebar_visible(driver):
    # Replace with the identifier or selector for the sidebar
    sidebar_locator = (By.ID, "sideNav")
    try:
        # Check if the sidebar element exists (without visibility check)
        sidebar = driver.find_element(*sidebar_locator)
        # Get the classes applied to the sidebar element
        sidebar_classes = sidebar.get_attribute("class").split()
        # Print the classes for debugging purposes
        print("Sidebar classes:", sidebar_classes)
        # Check if the sidebar element has the "visible" class
        return "visible" in sidebar_classes
    except:
        return False

def is_community_dropdown_visible(driver):

    try:
        # Wait for the sidebar to be visible
        sidebar_locator = (By.ID, "sideNav")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(sidebar_locator))
        
        # Find the list item (<li>) for "Community" within the sidebar
        community_list_item_locator = (By.ID, "menu-item-249")
        community_list_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located(community_list_item_locator))
        
        #wait until the elements become interactable
        time.sleep(4)
        # Click on the list item to trigger the interaction with the anchor tag inside it
        community_list_item.click()
    
        # Wait for the dropdown to be visible
        dropdown_locator = (By.CSS_SELECTOR, "li#menu-item-249 ul.sub-menu")
        dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
        # Get the classes applied to the dropdown element
        dropdown_classes = dropdown.get_attribute("class").split()
        # print the classes fr debugging purposes
        print("Dropdown classes:", dropdown_classes)
        # Check if the "side-nav-visible" attribute is present in the "dropdown classes" class
        return "side-nav-visible" in dropdown_classes
    except Exception as e:
        # If any errors occur, print the error message
        print("Test failed:", str(e))
        return False

def is_privacy_dropdown_visible(driver):

    try:
        # Wait for the sidebar to be visible
        sidebar_locator = (By.ID, "sideNav")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(sidebar_locator))

        # Find the list item (<li>) for "Privacy" within the sidebar
        community_list_item_locator = (By.ID, "menu-item-512")
        community_list_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located(community_list_item_locator))

        #wait until the elements become interactable
        time.sleep(4)
        # Click on the list item to trigger the interaction with the anchor tag inside it
        community_list_item.click()

        # Wait for the dropdown to be visible
        dropdown_locator = (By.CSS_SELECTOR, "li#menu-item-512 ul.sub-menu")
        dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
        # Get the classes applied to the dropdown element
        dropdown_classes = dropdown.get_attribute("class").split()
        # print the classes fr debugging purposes
        print("Dropdown classes:", dropdown_classes)
        # Check if the "side-nav-visible" attribute is present in the "dropdown classes" class
        return "side-nav-visible" in dropdown_classes
    except Exception as e:
        # If any errors occur, print the error message
        print("Test failed:", str(e))
        return FalseAOA


def test_sidebar_open(driver):
    try:
        # Replace with the identifier or selector for the burger icon
        burger_icon_locator = (By.ID, "burger")
        burger_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located(burger_icon_locator))

        # Click on the burger icon
        burger_icon.click()
        
        assert is_sidebar_visible(driver), "Sidebar not visible after clicking the burger icon."
        
        print("Sidebar opened successfully!")

        assert is_community_dropdown_visible(driver), "Community dropdown not visible after clicking the 'Community' li tag."

        print("Community dropdown shown successfully!")

        assert is_privacy_dropdown_visible(driver), "Privacy dropdown not visible after clicking the 'Privacy' li tag."

        print("Privacy dropdown shown successfully!")        

    except Exception as e:
        # If any errors occur, print the error message
        print("Test failed:", str(e))
