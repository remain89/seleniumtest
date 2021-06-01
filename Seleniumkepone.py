from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import keponefunction

chromedriver='C:\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)

phone="01227717182"

driver.get('http://59.3.93.125:8085/aimir/login')
keponefunction.Login(driver)
time.sleep(6)
keponefunction.LPDownload(driver,phone)
keponefunction.GMMPTest(driver,phone)