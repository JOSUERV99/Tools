import bs4, os
from urllib.request import urlopen
from bs4 import BeautifulSoup 

"""
    Objective: get the data from the page below, and generate a JSON file with the information of the products
"""

url = 'https://www.amazon.com/-/es/b?node=16225007011&pf_rd_p=af9fd607-7c8d-4628-8c4c-f4e2c44f8d63&pf_rd_r=47MCA21T6M2RNCGREXEB'
#os.system('cls')
print("Loading page")
#url_get = urlopen(url) # give the url of the page that you want to get
page_html = open('SM_TEC.html', 'r') # get the html file
#url_get.close()

soup = BeautifulSoup( page_html, "html.parser" ) #object to manipulate the html
logs = soup.findAll("table", {"class": "table table-condensed"})
r = logs.find("tr")
print(logs)
print(len(r), r)

#TODO: read the doc for get elements by class name
#TODO: sort the code into functions