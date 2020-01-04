import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup 

"""
    Objective: get the data from the page below, and generate a JSON file with the information of the products
"""

url = 'https://www.amazon.com/-/es/b?node=16225007011&pf_rd_p=af9fd607-7c8d-4628-8c4c-f4e2c44f8d63&pf_rd_r=47MCA21T6M2RNCGREXEB'

print("Loading page")
url_get = urlopen(url) # give the url of the page that you want to get
page_html = url_get.read() # get the html file
url_get.close()

page_soup = BeautifulSoup( page_html, "html.parser" ) #object to manipulate the html
print(page_soup.h1)

containers = page_soup.findAll("div", {"class": "s-item-container"})
products_title = page_soup.findAll("div", {"class": "a-row a-spacing-none"})
products_info = {}

#TODO: read the doc for get elements by class name
#TODO: sort the code into functions