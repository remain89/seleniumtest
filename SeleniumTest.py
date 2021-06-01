from selenium import webdriver
import time



# 브라우저의 사이즈 지정(화면 사이즈에 따라서 동적으로 엘리멘트가 변하는 경우 필요할듯)
### webdriver_options .add_argument('windows-size=1920x1080')
# 그래픽 카드 사용하지 않음
### webdriver_options .add_argument('disable-gpu')
# http request header의 User-Agent 변조, 기본으로 크롤링 할 경우
# 이 정보는 크롬 헤드리스 웹드라이버로 넘어가므로 똑똑한 웹서버는
# 이 정보를 보고 응답을 안해줄수도 있는데 이걸 피하기 위해 변조할수있다.
### webdriver_options .add_arguemnt('User-Agent: xxxxxxxxxxxxxxx')
# 사용자 언어
### webdriver_options .add_arguemnt('lang=ko_KR')

# Chrome 창이 뜨지 않도록 하는 옵션, 근데 파이참이 먹통이됨
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')

chromedriver = 'C:\chromedriver.exe'
driver = webdriver.Chrome(chromedriver,options=webdriver_options) #뒤에 옵션 추가

driver.get('https://auto.naver.com/bike/mainList.nhn')

print("+" * 100)
print(driver.title)
print(driver.current_url)
print("바이크 브랜드 크롤링")
print("-" * 100)

# 바이크 제조사 전체 페이지 버튼 클릭
bikeCompanyAllBtn = driver.find_element_by_css_selector("#container > div.spot_main > div.spot_aside > div.tit > a")
bikeCompanyAllBtn.click()

time.sleep(3)

# 바이크 제조사 1번 페이지 진입해서 바이크 리스트 추출
allBikeCompanyElement = driver.find_elements_by_css_selector(
    "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")

# 바이크 첫 페이지 크롤링
for item in allBikeCompanyElement:
    bikeComName = item.find_element_by_tag_name("span").text
    if (bikeComName != ''):
        print("바이크 회사명:" + bikeComName)
        ahref = item.find_element_by_tag_name("a").get_attribute("href")
        print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
        imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
        print('바이크 회사 엠블럼:', imgUrl)

time.sleep(3)

# 바이크 제조사 리스트의 다음 페이지 버튼을 찾아서 클릭하자.
nextBtn = driver.find_element_by_css_selector(
    "#_vendor_select_layer > div > div.maker_group > div.rolling_btn > button.next")
# 다음 바이크 제조사 페이지 버튼이 활성화 여부
isExistNextPage = nextBtn.is_enabled()

if (isExistNextPage == True):
    print("다음 페이지 존재함=======================================>")
    nextBtn.click()
    allBikeCompanyElement = driver.find_elements_by_css_selector(
        "#_vendor_select_layer > div > div.maker_group div.emblem_area > ul > li")
    for item in allBikeCompanyElement:
        bikeComName = item.find_element_by_tag_name("span").text
        if (bikeComName != ''):
            print("바이크 회사명:" + bikeComName)
            ahref = item.find_element_by_tag_name("a").get_attribute("href")
            print('네이버 자동차 바이크제조사 홈 sub url:', ahref)
            imgUrl = item.find_element_by_tag_name("img").get_attribute("src")
            print('바이크 회사 엠블럼:', imgUrl)

# 크롤링이 끝나면 webdriver 브라우저를 종료한다.
# driver.quit()