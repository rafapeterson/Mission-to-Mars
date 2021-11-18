# Import Splinter & BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

# visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_not_present_by_css('div.list_text', wait_time=1)

# Set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_="content_title")

# Use the parent element to find the first 'a' tag & save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use parent element to find paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images
# 

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting HTML with soup
html = browser.html
img_soup = soup(html, 'html')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# scrape table data
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

#browser.quit()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 

# 

# ### Hemispheres

# 1. Use browser to visit the URL
# Visit the USGS Astrogeology Science Center Site
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser("chrome", **executable_path, headless=True)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# 3. Write code to retrieve the image urls and titles for each hemisphere.
# find links w/ class "itemLink product-item" & click. Find first <h3> and click link named sample.
# add url to list as image_url, and then copy h2 as the title



# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for link in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[link].click()
    
    # get url for image
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Add what was scraped to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()


hemisphere_image_urls   



# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls



browser.quit()

