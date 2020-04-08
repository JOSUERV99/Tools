"""
@objective Tools for webscrapping with bs4 and selenium
@author josuerv99
@since 7/4/2020
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = r'chromedriver.exe'

def getSorucePage(url):
    incog_mode = Options()
    incog_mode.add_argument('--incognito')
    browser = webdriver.Chrome(driver_path, options=incog_mode)
    browser.get(url)
    source = browser.page_source
    browser.close()
    return source

def saveHtmlFile(string, filename='page.html'):
    with open(filename, 'w') as f:
        f.write(string)
    
def getTextFromHtmlFile(filename):
    
    pass

url = 'http://www.google.com'
pageSoruce = getSorucePage(url)
saveHtmlFile(pageSoruce)

