#%%
from selenium import webdriver
#%%
url = 'https://www.districtwestapts.com/floorplans'
a = os.getcwd() 
browser = webdriver.Chrome()
browser.get(url)

# %%
