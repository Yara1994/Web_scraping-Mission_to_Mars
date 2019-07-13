# import dependencies

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as import pd
import requests

def scrape_all():

    # Choose the executable path to driver 
 
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    data = {

        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser)

    }

    return data

def mars_news(browser):

    # Visit Nasa news url through splinter module

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Parse HTML with Beautiful Soup

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    return news_title, news_p


def featured_image(browser):

    return img_url

