#%%
from selenium import webdriver
#%%
url = 'https://www.districtwestapts.com/floorplans'
a = os.getcwd() 
browser = webdriver.Chrome('/Users/ubaidrahim/Desktop/env/chromedriver')
browser.get(url)

# %%
d = okay next