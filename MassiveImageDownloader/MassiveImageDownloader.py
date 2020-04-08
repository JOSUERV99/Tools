"""
@objective download n images and saved in a folder given a target 
@author: Josué Rojas Vega
@since: 07/04/2019
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from cv2 import imshow, imread, imwrite
from random import randint
import requests, shutil, os

class MassiveImageDownloader:
    
    default_path = r'images'
    main_url = r'https://www.google.com/imghp?hl=es'
    driver_path = r'chromedriver.exe'
    
    @staticmethod
    def initBrowser():
        print("Initializing...")
        incogniteMode = (Options()).add_argument('--incognito')
        browser = webdriver.Chrome(MassiveImageDownloader.driver_path, options=incogniteMode)
        browser.get(MassiveImageDownloader.main_url)
        return browser
    
    @staticmethod
    def search(browser, target):
        print("Searching images....")
        searchBox = browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        searchBox.send_keys(target)
        firstOption = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/ul/li[1]')
        firstOption.click()
        image_elements = browser.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]')
        images = image_elements.find_elements_by_tag_name('img')
        return images
    
    @staticmethod
    def downloadImages(imageObjects, searchTarget, downloadsQuantity=1, folder=default_path):
        def saveImage(link, filename='img.png'):
            response = requests.get(link, stream=True)
            with open(filename, 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        def createDirectory(dir):
            try:
                os.stat(dir)
            except:
                os.mkdir(dir)
        print("Creating directory...")
        createDirectory(folder)
        os.chdir(folder)
        print("{} images were found\n\nDownloading...".format(len(imageObjects)))
        images_downloadeds = []
        for n in range(downloadsQuantity):
            # picking image
            random_index = randint(0, len(imageObjects))
            while (imageObjects[random_index] in images_downloadeds):
                random_index = randint(0, len(imageObjects))
            # get download link
            link = imageObjects[random_index].get_attribute('src')
            # download and save image
            img_name = f'{searchTarget}_{random_index}_{n}.png'
            print('Downloading {}'.format(img_name))
            saveImage(link, filename=img_name)
    
    @staticmethod
    def doIt(target='', quantity=10, folder=default_path):
        try:
            browser = MassiveImageDownloader.initBrowser()
            imageWebElements = MassiveImageDownloader.search(browser, target)
            MassiveImageDownloader.downloadImages(imageWebElements, target, downloadsQuantity=quantity, folder=folder)
        except Exception as e:
            print(e)
        finally:
            if (browser != None):
                browser.close()

#TODO: fix selection in context menu to download
#MassiveImageDownloader.doIt(target='sunsets', quantity=1, folder='img_sunsets')

