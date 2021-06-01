from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import keponefunction

chromedriver='C:\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)

driver.get('http://59.3.93.125:8085/aimir/login')
keponefunction.Login(driver)
time.sleep(6)
keponefunction.LPDownload(driver,"01227717182")
keponefunction.GMMPTest(driver,"01227717182")