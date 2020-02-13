#!/usr/bin/env python
# coding: utf-8

# In[37]:

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import selenium
from selenium import webdriver


# In[38]:


def init_browser(): 
    executable_path = {'executable_path': '/chromedriver/79.0.3945.36/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


# In[39]:


#init_browser()


# In[40]:


def mars_news():
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find("div",class_="content_title").text
    news_content = soup.find("div",class_="article_teaser_body").text
    news_date = soup.find("div",class_="list_date").text
    return news_title, news_content, news_date


# In[41]:


#mars_news()


# In[42]:


def mars_image():
    browser = init_browser()
    base_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(base_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    
    return featured_image_url


# In[43]:


#mars_image()


# In[44]:


def mars_weather():
    response_w=requests.get('https://twitter.com/marswxreport?lang=en')
    soup = BeautifulSoup(response_w.text)
    mars_weather_s= soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather = mars_weather_s
    return mars_weather


# In[45]:


#mars_weather()


# In[46]:


def mars_facts():
    tables =pd.read_html('https://space-facts.com/mars/')
    df=tables[0]
    df.columns=['Description','Value']
    df.set_index(df['Description'],inplace=True)
    del df['Description']
    return df


# In[47]:


#mars_facts()


# In[48]:


def mars_hemispheres():
    list_of_url = ['cerberus_enhanced','schiaparelli_enhanced','syrtis_major_enhanced','valles_marineris_enhanced']
    url_final = [f'https://astrogeology.usgs.gov/search/map/Mars/Viking/{element}' 
             for element in list_of_url]
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
        
    return mars_hemisphere


# In[49]:


#mars_hemispheres()


# In[50]:


def scrape():
    
    data_dict = {}
    mars_news_split = mars_news()
    data_dict['mars_news'] = mars_news_split[0]
    data_dict['mars_paragraph'] = mars_news_split[1]
    data_dict['mars_date'] = mars_news_split[2]
    data_dict['mars_image'] = mars_image()
    data_dict["mars_weather"] = mars_weather()
    data_dict["mars_facts"] = mars_facts()
    mars_hemispheres_split = mars_hemispheres()
    data_dict["mars_hemisphere1"] = mars_hemispheres_split[0]['img_url']
    data_dict["mars_hemisphere1_title"] = mars_hemispheres_split[0]['title']
    data_dict["mars_hemisphere2"] = mars_hemispheres_split[1]['img_url']
    data_dict["mars_hemisphere2_title"] = mars_hemispheres_split[1]['title']
    data_dict["mars_hemisphere3"] = mars_hemispheres_split[2]['img_url']
    data_dict["mars_hemisphere3_title"] = mars_hemispheres_split[2]['title']
    data_dict["mars_hemisphere4"] = mars_hemispheres_split[3]['img_url']
    data_dict["mars_hemisphere4_title"] = mars_hemispheres_split[3]['title']

    
    

    return data_dict


# In[ ]:




