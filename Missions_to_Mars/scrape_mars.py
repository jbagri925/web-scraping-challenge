# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#import dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import os
import pandas as pd
import time
import requests
browser = Browser('chrome', headless=True)


# %%
#visiting the page
def scrape_mars_news():
    try: 
        # Initialize browser 
        browser = init_browser()
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
# %%
#using bs to write it into html
html = browser.html
soup = bs(html,"html.parser")
news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")

       return mars_info
           finally:

        browser.quit()

# %%
#Visit the url for JPL Featured Space Image
def scrape_mars_image():

    try: 
        # Initialize browser 
        browser = init_browser()
url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_image)

return mars_info
finally:

        browser.quit()

# %%
# visit the mars weather report twitter and scrape the latest tweet
def scrape_mars_weather():

    try: 
        # Initialize browser 
        browser = init_browser()
mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
time.sleep(1)
mars_weather_html = browser.html
mars_weather_soup = BeautifulSoup(mars_weather_html, 'html.parser')
latest_tweets = soup.find_all('div', class_='js-tweet-text-container')


# %%
# Search Within Tweet for <p> Tag Containing Tweet Text
mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
print(mars_weather)

return mars_info
finally:
        browser.quit()
# %%
# visit space facts and scrap the mars facts table

def scrape_mars_facts():
     # Initialize browser 
        browser = init_browser()
mars_facts_url = 'https://space-facts.com/mars/'
browser.visit(mars_facts_url)
time.sleep(1)
mars_facts_html = browser.html
mars_facts_soup = BeautifulSoup(mars_facts_html, 'html.parser')

print(mars_facts)

return mars_data
finally:
        browser.quit()
# %%
# Visit the Mars Facts Site Using Pandas to Read
mars_df = pd.read_html("https://space-facts.com/mars/")[0]
print(mars_df)
mars_df.columns=["Description", "Value"]
mars_df.set_index("Description", inplace=True)
mars_df


# %%
# Visit the USGS Astrogeology Science Center Site
def scrape_mars_hemispheres():

    try: 

        # Initialize browser 
        browser = init_browser()

url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hemisphere)


# %%
# HTML Object
html_hemispheres = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_hemispheres, 'html.parser')

# Retreive all items that contain mars hemispheres information
items = soup.find_all('div', class_='item')

# Create empty list for hemisphere urls 
hemisphere_image_urls = []

# Store the main_ul 
hemispheres_main_url = 'https://astrogeology.usgs.gov'

# Loop through the items previously stored
for i in items: 
    # Store title
    title = i.find('h3').text
    
    # Store link that leads to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Visit the link that contains the full image website 
    browser.visit(hemispheres_main_url + partial_img_url)
    
    # HTML Object of individual hemisphere information website 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
    soup = BeautifulSoup( partial_img_html, 'html.parser')
    
    # Retrieve full image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
        # Append the retreived information into a list of dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

       # Return mars_data dictionary 

        return mars_info
    finally:

        browser.quit()
    

# Display hemisphere_image_urls
hemisphere_image_urls


# %%



