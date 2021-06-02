from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def Login(driver): #Step1 로그인
    id=driver.find_element_by_name('j_username')
    id.send_keys('admin')
    pw=driver.find_element_by_name('j_password')
    pw.send_keys('nuri1234')
    driver.find_element_by_id('login').click()

def LPDownload(driver,pnumber): #Step2 LP 데이터 검색 후 엑셀 다운로드
    element=driver.find_element_by_link_text('검침 정보') # 검침정보창 열기
    hov=ActionChains(driver).move_to_element(element)
    hov.perform()
    driver.find_element_by_link_text('사용량 조회').click() # 사용량정보창 열기
    hov.reset_actions() #안먹힘

    phonenum=driver.find_element_by_xpath("//input[@id='textfield-1195-inputEl']") # 검색
    phonenum.send_keys(pnumber)
   # driver.find_element_by_xpath("//div[@class='x-btn x-btn-search x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']").click()
    phonenum.send_keys(Keys.RETURN)  # 모뎀번호에서 엔터눌러서 검색
    time.sleep(2)

    driver.find_element_by_xpath("//div[@id='button-1134']").click() # 저장
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='button-1006']").click() # 확인창
    time.sleep(2)
    driver.find_element_by_xpath("//a[@id='tab-1215-closeEl']").click() # 사용량정보창 종료

def GMMPTest(driver,pnumber): #Step3 모뎀 설정 조회
    element=driver.find_element_by_link_text('모뎀관리') # 검침정보창 열기
    hov=ActionChains(driver).move_to_element(element)
    hov.perform()
    driver.find_element_by_link_text('모뎀 환경 설정').click() # 환경설정 창 열기
    hov.reset_actions() # 안먹힘

    phonenum=driver.find_element_by_xpath("//input[@id='textfield-1103-inputEl']") # 결과 확인
    phonenum.send_keys(pnumber)
    driver.find_element_by_xpath("//div[@id='button-1107']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='checkboxfield-1182-inputEl']").click()
    driver.find_element_by_xpath("//input[@id='checkboxfield-1184-inputEl']").click()
    driver.find_element_by_xpath("//input[@id='checkboxfield-1190-inputEl']").click()
    driver.find_element_by_xpath("//input[@id='checkboxfield-1196-inputEl']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='button-1218']").click()

    time.sleep(30)
    driver.find_element_by_xpath("//a[@id='tab-1437-closeEl']").click() # 환경창 종료

def LPCheck(driver,pnumber): #Step4 검색 시점의 당일 LP 갯수가 맞는가
    element=driver.find_element_by_link_text('검침 정보') # 검침정보창 열기
    hov=ActionChains(driver).move_to_element(element)
    hov.perform()
    driver.find_element_by_link_text('사용량 조회').click() # 사용량정보창 열기
    hov.reset_actions() #안먹힘

    phonenum=driver.find_element_by_xpath("//input[@id='textfield-1195-inputEl']") # 검색
    phonenum.send_keys(pnumber)
    #driver.find_element_by_xpath("//div[@class='x-btn x-btn-search x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']").click() #검색버튼 클릭
    phonenum.send_keys(Keys.RETURN) #모뎀번호에서 엔터눌러서 검색
    time.sleep(2)
    number=driver.find_element_by_xpath("//div[@id='tbtext-1126']").text
    choice=number[4:6] # 검색 시점의 LP 총 갯수
    choice=int(choice)
    now=datetime.now()
    checknum=int((now.hour*4)+(now.minute/15))
    print("시간으로 계산된 갯수 "+str(checknum))

    snum=0
    sumnum=driver.find_elements_by_xpath("//*[contains(text(), '전체')]")

    for i in sumnum :
        snum=snum+1
    snum=snum-6

    if (snum*choice)>100 :
        choice = number[4:7]  # 검색 시점의 LP 총 갯수

    print("검침 총 갯수 " + str(choice))
    print("모뎀에 연결된 미터 갯수는 "+str(snum))
    print("보유해야할 LP 갯수는 "+str(checknum*snum))
    print("-----결과-----")
    if (checknum*snum)==choice :
        print("LP 데이터 수량 일치")
    else :
        print("LP 데이터 수량 불일치, 확인이 필요함")
#    driver.find_element_by_xpath("//a[@id='tab-1215-closeEl']").click()  # 사용량정보창 종료