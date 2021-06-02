from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import keponefunction

chromedriver='C:\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)

#phone="01227717182" # 모뎀 전화번호 1개
phone="01232973665" # 모뎀 전화번호 복수


driver.get('http://59.3.93.125:8085/aimir/login')
keponefunction.Login(driver)
time.sleep(6)
#keponefunction.LPDownload(driver,phone)
#keponefunction.GMMPTest(driver,phone)
keponefunction.LPCheck(driver,phone)

driver.quit() # 창 종료