# import dependencies

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests



# Initialize browser

def init_browser():

    # Choose the executable path to driver 
 
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# Create Mission to Mars global dictionary that can be imported into Mongo

mars_info = {}



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

    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_p

    # Close the browser after scraping

    browser.quit()

    return mars_info

    

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

    return mars_info


# WEATHER TWEET

def mars_weather():

    # Initialize browser 

    browser = init_browser()

    # Visit Mars Weather Twitter through splinter module

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    # Parse HTML with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Find all elements that contain tweets

    tweets = soup.find_all("div", class_= "js-tweet-text-container")

    # Retrieve all elements that contain news title in the specified range
    # Look for entries that display weather related words
    # to exclude non weather related tweets

    for tweet in tweets: 
        mars_weather = tweet.find('p').text 

    # Dictionary entry from WEATHER TWEET

    mars_info['weather_tweet'] = mars_weather

    browser.quit()

    return mars_info


# MARS FACTS

def mars_facts():

    # Initialize browser 

    browser = init_browser()

    # Visit Mars facts url 

    url = "https://space-facts.com/mars/"
    browser.visit(url)

    # Use Panda's `read_html` to parse the url

    mars_facts = pd.read_html(url)

    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`

    mars_df = mars_facts[1]

    # Assign the columns `['Description', 'Value']`

    mars_dataframe = mars_df.rename(columns = {0 : "Description", 1 : "Value"})

    # Set the index to the `Description` column

    mars_df = mars_dataframe.set_index("Description")

    # Save html code to folder Assets

    data = mars_df.to_html()

    # Dictionary entry from MARS FACTS

    mars_info['mars_facts'] = data

    browser.quit()

    return mars_info


# MARS HEMISPHERES

def mars_hemispheres():

    # Initialize browser 

    browser = init_browser()

    # Visit Mars Hemispheres through splinter module

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    # Parse HTML with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retreive all items that contain mars hemispheres information

    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 

    hemisphere_image_urls = []

    # Store the main_ul

    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored

    for item in items: 
        
        # Store title
        
        title = item.find('h3').text
        
        
        # Store link that leads to full image website
        
        partial_img_url = item.find('a', class_='itemLink product-item')['href']
        
        
        # Visit the link that contains the full image website 
        
        browser.visit(hemispheres_main_url + partial_img_url)
        
        # Parse HTML with Beautiful Soup for every individual hemisphere information website
        
        partial_img_html = browser.html
        soup = BeautifulSoup(partial_img_html, 'html.parser')
        
        # Retrieve full image source 
        
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        
        # Append the retreived information into a list of dictionaries
        
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    #Dictionary entry from WEATHER TWEET

    mars_info["hemisphere_image_urls"] = hemisphere_image_urls

    browser.quit()

    return mars_info


    












    

