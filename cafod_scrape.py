from selenium import webdriver
import time
from threading import Thread
import csv
import pandas as pd
import re
from secrets import email, password



chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


# VARIABLE CONSTANTS

FACEBOOK_EMAIL = email
FACEBOOK_PASSWORD = password

def cafod_scrape_func():

    ## Later change this to an input where the user can put in their own organisation and the scrape will work from there
    # organisation_to_scrape = input("Type the Organisation as shown for what you would like to scrape: \n CAFOD \n amnesty \n savethechildrenuk \n oxfaminsouthsudan/ \n   ")
    organisation_to_scrape = 'CAFOD'

    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get('https://www.facebook.com')
    time.sleep(3)
    button = browser.find_element_by_xpath("//*[@id='u_0_k']") # this was changed for some reason
    button.click()
    time.sleep(1)
    button = browser.find_element_by_xpath("//*[@id='email']")
    button.send_keys(FACEBOOK_EMAIL)
    button = browser.find_element_by_xpath("//*[@id='pass']")
    button.send_keys(FACEBOOK_PASSWORD)
    button = browser.find_element_by_xpath("//*[@id='u_0_b']")
    button.click()
    time.sleep(2)
    browser.get(f'https://www.facebook.com/{organisation_to_scrape}')
    time.sleep(2)
    # Getting the Organisations name
    handle = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div[1]/h2")
    handle = handle.text
    # Getting the organisations profile picture
    profile_image = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/a").get_attribute("href")
    # Getting the organisations banner picture
    banner_image = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div[2]/div/a/div/div/div/div/img").get_attribute("src")

    
    button = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div[2]/div/div/span/div/div/span/div[2]/div/div")
    button.click()
    # Getting the about description for the Organisation
    about_description = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[1]/div/div/div/div[2]")
    about_description = about_description.text

    # Get the number of followers the organisation has
    followers = browser.find_element_by_xpath("//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[5]/div/div/div/div[2]/div/div/span/span").text
    

    SCROLL_PAUSE_TIME = 4

    no_of_target_posts = 40
    posts_increment = 1
    likes_per_post = []
    # list_of_shares = []
    for i in range(1, no_of_target_posts):
        #browser.execute_script("window.scrollBy(0, 600);")
        browser.execute_script("window.scrollBy(0, 800);")
        time.sleep(SCROLL_PAUSE_TIME)

        pass_in_param = str(f"//*[@id='mount_0_0']/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/div/div[{posts_increment}]/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[1]/div/span/div/span[2]/span")
        likes_on_post = browser.find_element_by_xpath(pass_in_param).text
        print(likes_on_post)
        likes_per_post.append(likes_on_post)
        posts_increment += 1


    print(likes_per_post)
    # print(shares_on_post)

    likes_per_post = [int(i) for i in likes_per_post] 
    lowest_num_of_likes = min(likes_per_post)
    highest_num_of_likes = max(likes_per_post)

    avg_likes_per_lost = sum(likes_per_post) // len(likes_per_post)
    print(avg_likes_per_lost)


    organisations_list = []

    organisation = {
        'Facebook Handle': handle,
        'Facebook Image URL': profile_image,
        'Facebook Banner URL': banner_image,
        'Facebook About': about_description,
        'No Of Followers': followers,
        'Lowest Like On Post': lowest_num_of_likes,
        'Highest Like On Post': highest_num_of_likes,
        'Average Like On Each Post': avg_likes_per_lost
        # 'Average Number Of Shares Per Post': 
    }
    organisations_list.append(organisation)



    df = pd.DataFrame(organisations_list)

    df.to_csv(f'{organisation_to_scrape} scrape.csv')