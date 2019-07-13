# import dependencies

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as import pd
import requests



# Initialize browser

def init_browser():

    # Choose the executable path to driver 
 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# Create Mission to Mars global dictionary that can be imported into Mongo

mars_data = {}



# NASA MARS NEWS

def mars_news():

    # Initialize browser 

    browser = init_browser()

    # Visit Nasa news url through splinter module

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Parse HTML with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Dictionary entry from MARS NEWS

    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p

    # Close the browser after scraping

    browser.quit()

    return mars_data

    

# FEATURED IMAGE

def mars_image():

    # Initialize browser 

    browser = init_browser()

    # Visit Mars Space Images through splinter module

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Have to click on "full image" button

    full_image_elem = browser.find_by_id("full_image")
    full_image_elem.click()

    # Have to click on "more info" button

    more_info_elem = browser.find_link_by_partial_text("more info")
    more_info_elem.click()

    # Parse HTML with Beautiful Soup

    html = browser.html
    img_soup = BeautifulSoup(html, "html.parser")

    # Display image link

    img_url_rel = img_soup.select_one("figure.lede a img").get("src")
    
    # main link

    main_url = "https://www.jpl.nasa.gov"

    # combine main link and image link

    featured_image_url = main_url + img_url_rel

    # Dictionary entry from FEATURED IMAGE

    mars_info['featured_image_url'] = featured_image_url

    # Close the browser after scraping

    browser.quit()

    return mars_data








    

