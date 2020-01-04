"""
@author: Josué Rojas Vega
@since: 01/01/2019
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, json

chrome_driver_path = r"C:\Users\JRV\Desktop\WebCrawling with Selenium (Python)\chromedriver.exe"
initial_page = r"https://tec-appsext.itcr.ac.cr/Matricula/frmAutenticacion.aspx?ReturnUrl=%2fmatricula"
credentials = {"username":"josuerojasvega@gmail.com", "key":"Xrl2qpjarV.TEC"}
filename = "courses.txt"

#options for initialize chrome
def getChromeDriver(driverPath, url):
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(driverPath, chrome_options=options) #open chrome
    driver.get(url)  #enter to the page
    return driver

#login 
def login(credentials, driver):
    username_field = driver.find_element_by_name("txtUsuario")
    username_field.send_keys(credentials["username"])
    password_field = driver.find_element_by_name("txtPassword")
    password_field.send_keys(credentials["key"])
    submit = driver.find_element_by_name("btnEntrar")
    submit.click()    

# initial dialog to choose the course period (example: )
def selectCourseStage(driver):
    # choose stage
    button_course = driver.find_elements_by_class_name("btn_Consultar")[1] #second option
    button_course.click()

# schedule
def getCoursesData(filename, driver):
    schedule_table = driver.find_element_by_id("tBodyCursos")
    #file = open("schedule.txt", "w") css_selector = #divHCI1107 > div > table
    info = schedule_table.find_element_by_xpath("//*[@id='tBodyCursos']/tbody")
    file = open(filename, "w")
    file.write(info.text)
    file.close()

def logout(driver):
    #TODO: fix ->  solved by using incognite mode of Chrome
    #driver.execute_script("document.getElementsByClassName('ui-button ui-widget ui-state-default ui-corner-all')[0].click()")
    pass

def generateJSON(driver, filename):
    #TODO: like a dict
    pass

print("opening chrome...")
driver = getChromeDriver(chrome_driver_path, initial_page)
login(credentials, driver)
selectCourseStage(driver)
getCoursesData(filename, driver)
print("logout...")
#logout(driver)
print("closing chrome...")
#driver.close() # close the chrome navigator
