import time
from selenium.webdriver.common.by import By

def open_single_post(driver):
    driver.implicitly_wait(10)
    post_link = driver.find_element(By.CLASS_NAME, 'hero-href')
    
    #click to open post
    post_link.click()
    print('post opened successfully')
    
    time.sleep(10)

def click_buttons(driver):
    btn_like = driver.find_element(By.ID, 'mp-rp-btn-like')
    btn_dislike = driver.find_element(By.ID, 'mp-rp-btn-dislike')
    btn_share = driver.find_element(By.ID, 'btn-share')
    btn_comment = driver.find_element(By.ID, 'btn-comment')
    btn_vote_checkbox = driver.find_element(By.ID, 'vote-checkbox')
    btn_bookmark = driver.find_element(By.ID, 'btn-bookmark')

    btn_like.click()
    print('like button clicked successfully')
    
    btn_dislike.click()
    print('dislike button clicked successfully')
    
    btn_share.click()
    print('share button clicked successfully')

    close_share_list = driver.find_element(By.ID, 'shareList-close')
    close_share_list.click()
    is_closed = close_share_list.is_displayed()
    assert not is_closed
    print('share list closed successfully')

    btn_comment.click()
    btn_comment.click()
    print('comment button clicked successfully')
    
    btn_vote_checkbox.click()
    print('vote checkbox clicked successfully')
    
    btn_bookmark.click()
    print('bookmark button clicked successfully')

    driver.quit()