from pickle import TRUE
from tkinter.tix import Select
#from types import NoneType
from attr import NOTHING
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import time
import pandas as pd
import os
import sys
import csv
from bs4 import BeautifulSoup
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



#This code is meant to webscrape the first page of forums incel.is forums, this code is a modification of the incel.py to scrape all forums on page 1
#Driver Intiation


def scrapeoneforum(urltop:str): 

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    #TJIS isi the best wy tp use the firefox because it doublechcks your browser and if te webdriver is not instaed it will do it for you. 
    # Selection of website
    driver.get(urltop)

    lst = list(range(1,3+1))
    for i in lst: 

    #ThreadName
        url4='/html/body/div[1]/div[4]/div/div[2]/div[1]/h1'
        w=driver.find_element(By.XPATH,url4).text
    #Username
        url='/html/body/div[1]/div[4]/div/div[3]/div/div/div[1]/div[3]/div/article['+str(i)+']/div/div[1]/section/div[2]/h4/span/span'
        b=driver.find_element(By.XPATH,url).text
    #Date
        url2='/html/body/div[1]/div[4]/div/div[3]/div/div/div[1]/div[3]/div/article['+str(i)+']/div/div[2]/div/header/ul[1]/li/a/time'
        c=driver.find_element(By.XPATH,url2).get_attribute('datetime')
    #message
        url3='/html/body/div[1]/div[4]/div/div[3]/div/div/div[1]/div[3]/div/article['+str(i)+']/div/div[2]/div/div/div[1]/article/div[1]'
        d=driver.find_element(By.XPATH,url3).text

    #writing to CSV
                
        data=[w,b,c,d]
        #outputfilename
       
        with open('output.csv', 'a', encoding='UTF8', newline='') as f:
            writer= csv.writer(f)
            writer.writerow(data)
