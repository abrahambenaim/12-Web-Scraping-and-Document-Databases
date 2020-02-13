#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import selenium
from selenium import webdriver


# In[2]:


executable_path = {'executable_path': '/usr/local/Caskroom/chromedriver/79.0.3945.36/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# # NASA Mars News

# In[5]:


#Latest article on Mars website:
news_title = soup.find("div",class_="content_title").text
news_content = soup.find("div",class_="article_teaser_body").text
news_date = soup.find("div",class_="list_date").text
print(f"Title: {news_title}")
print(f"Content: {news_content}")
print(f"Date: {news_date}")


# # JPL Mars Space Images - Featured Image

# In[72]:


url_image = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url_image)


# In[73]:


html_i = browser.html
soup_i = BeautifulSoup(html_i, 'html.parser')


# In[74]:


image_button = browser.find_by_id("full_image").click()
next_link = browser.find_link_by_partial_text("more info").click()


# In[89]:


results_i = soup.find_all('img')


# In[90]:


results_i


# In[91]:


image_i_big = []
for result_i in results_i:
    big_image=result_i['src']
    image_i_big.append(big_image)
    
base_url = 'https://www.jpl.nasa.gov'
image_url=image_i_big[0]
featured_image_url=base_url+image_url
featured_image_url


# # Mars Live Weather

# In[92]:



response_w=requests.get('https://twitter.com/marswxreport?lang=en')
soup = BeautifulSoup(response_w.text)


# In[93]:


mars_weather_s= soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text


# In[94]:



mars_weather = mars_weather_s
mars_weather


# # Mars facts

# In[95]:


tables =pd.read_html('https://space-facts.com/mars/')
df=tables[0]
df.columns=['Description','Value']
df.set_index(df['Description'],inplace=True)
del df['Description']


# In[96]:


df


# # Mars hemispheres

# In[98]:


list_of_url = ['cerberus_enhanced','schiaparelli_enhanced','syrtis_major_enhanced','valles_marineris_enhanced']
url_final = [f'https://astrogeology.usgs.gov/search/map/Mars/Viking/{element}' 
             for element in list_of_url]


# In[99]:


mars_hemisphere = []
for idx,element in enumerate(url_final):
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url_final[idx])
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h2',class_='title').text
    picture = soup.li.a['href']
    mars_hemisphere.append({'title':title,'img_url':picture})


# In[100]:


mars_hemisphere


# In[ ]:




