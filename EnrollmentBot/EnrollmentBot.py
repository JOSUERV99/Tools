"""
@objective realize the enrollment process with a python bot
@author: Josué Rojas Vega
@since: 01/01/2019
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, json

chrome_driver_path = r'chromedriver.exe'
initial_page = r"https://tec-appsext.itcr.ac.cr/Matricula/frmAutenticacion.aspx?ReturnUrl=%2fmatricula"
credentials = {"username":"email", "key":'pass'}
filename = "courses.txt"

#options for initialize chrome
def getChromeDriver(driverPath, url=chrome_driver_path, arg="--incognito"):
    options = Options()
    options.add_argument(arg)
    driver = webdriver.Chrome(driverPath, chrome_options=options) #open chrome
    driver.get(url)  #enter to the page
    return driver

#login 
def login(driver, credentials):
    username_field = driver.find_element_by_name("txtUsuario")
    username_field.send_keys(credentials["username"])
    password_field = driver.find_element_by_name("txtPassword")
    password_field.send_keys(credentials["key"])
    submit = driver.find_element_by_name("btnEntrar")
    submit.click()    

# initial dialog to choose the course period (example: )
def selectCourseStage(driver):
    # choose stage
    button_course = driver.find_elements_by_class_name("btn_Consultar")[0] #choose period
    button_course.click()

# schedule
def getCoursesData(driver, filename='courses_info.txt'):
    schedule_table = driver.find_element_by_id("tBodyCursos")
    #file = open("schedule.txt", "w") css_selector = #divHCI1107 > div > table
    info = schedule_table.find_element_by_xpath("//*[@id='tBodyCursos']/tbody")
    file = open(filename, "w")
    file.write(info.text)
    file.close()

def generateJSON(driver, filename):
    #TODO: like a dict
    pass

def savePage(driver, filename='page_src.html'):
    page = driver.page_source
    with open(filename, 'w') as f:
        f.write(page)
    #print(page)


browser = getChromeDriver(chrome_driver_path, initial_page)
login(browser, credentials)
savePage(browser)
selectCourseStage(browser)
# getCoursesData(browser, filename='files/courses.txt')
# print("logout...")
# print("closing chrome...")
# driver.close() # close the chrome navigator
