import shutil
import subprocess
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chromeTemp = 'C:/chrometemp' #디버거 크롬의 쿠키, 캐시 파일 등이 저장될 경로
chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe' #chrome.exe의 경로
webdriverPath = 'C:/chromedriver.exe' #chromedriver.exe의 경로

CityProvince = "공학도" #시/도
SchoolLevel = "중학교" #학교급
SchoolName = "코딩중학교" #학교 이름
UserName = "김카힐" #이름
BirthDate = "000000" #생년월일
Password = "1234" #비밀번호

subprocess.Popen(chromePath + ' --remote-debugging-port=9222 --user-data-dir="' + chromeTemp + '" --headless https://hcs.eduro.go.kr/#/relogin')
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(webdriverPath, options=option)

sleep(0.5)

try:
    driver.find_element_by_id('password').click()
except:
    driver.find_element_by_id('btnConfirm2').click()
    
    #개인정보 입력 화면
    sleep(0.5)
    driver.find_element_by_id('schul_name_input').click()
    
    #학교 관련 정보 입력 화면
    sleep(0.5)
    Select(driver.find_element_by_id('sidolabel')).select_by_visible_text(CityProvince)
    sleep(0.5)
    Select(driver.find_element_by_id('crseScCode')).select_by_visible_text(SchoolLevel)
    sleep(0.5)
    driver.find_element_by_id('orgname').send_keys(SchoolName)
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    sleep(1.5)
    driver.find_element_by_css_selector("#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul").click()
    sleep(0.5)
    driver.find_element_by_class_name('layerFullBtn').click()
    
    #학교 관련 정보 입력 화면 닫음
    sleep(0.5)
    driver.find_element_by_id('user_name_input').send_keys(UserName)
    sleep(0.5)
    driver.find_element_by_id('birthday_input').send_keys(BirthDate)
    sleep(0.5)
    driver.find_element_by_id('btnConfirm').click()
    
    #비밀번호 입력 화면
    sleep(0.5)
    driver.find_element_by_id('password').click()

for i in list(Password):
    sleep(0.5)
    driver.find_element_by_css_selector(f'[aria-label="{i}"]').click()
sleep(0.5)
driver.find_element_by_id('btnConfirm').click()

#사용자 계정 선택 화면
sleep(1.5)
driver.find_element_by_xpath(f"//*[contains(text(), '{UserName}')]").click()

#질문 응답 화면
for i in range(1, 4):
    sleep(0.5)
    driver.find_element_by_css_selector(f"#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child({i}) > dd > ul > li:nth-child(1) > label").click()
driver.find_element_by_id('btnConfirm').click()

print("자가진단을 완료했습니다")
driver.close()
