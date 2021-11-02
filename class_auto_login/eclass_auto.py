import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/chromedriver"
driver = webdriver.Chrome(path)
driver.set_window_size(1600,1080)
driver.implicitly_wait(10)
driver.get("https://eclass.dongguk.edu/") # web page load

time.sleep(2)

'''
iframes = driver.find_elements_by_css_selector('frame')
print(iframes)
print('현재 페이지에 frame은 %d개가 있습니다.' % len(iframes))
'''

def killPopUp(frame1, frame2, _xpath_):
    # kill popup window by using selenium!! sibal
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath(frame1)) # frame # we have to refer frame - iframe
    driver.switch_to.frame(driver.find_element_by_xpath(frame2)) # iframe
    popupkill = driver.find_element_by_xpath(_xpath_)
    popupkill.click()

def select_class(_ClassXpath_):
    pass

try:
    killPopUp('/html/frameset/frame','//*[@id="modalIframeId"]','//*[@id="noMoreToday"]')
except:
    pass

# click red button for sending ID and PW
try:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame')) # frame # we have to refer frame - iframe

    login_click = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[1]/a')
    login_click.click()
except:
    pass

# send ID and PW , Login
try:
    time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame')) # frame # we have to refer frame - iframe

    login_ID = 'YOUR ID'
    login_PW = 'YOUR PASSWORD'

    elem = driver.find_element_by_xpath('//*[@id="id"]')
    elem.send_keys(login_ID)
    elem = driver.find_element_by_name("userDTO.password")
    elem.send_keys(login_PW)

    elem.send_keys(Keys.RETURN) # Enter Kry
except:
    pass

# kill popup1
try:
    killPopUp('/html/frameset/frame','//*[@id="modalIframeId"]','//*[@id="noMoreToday"]')
except:
    pass

# kill popup2
try:
    killPopUp('/html/frameset/frame','//*[@id="modalIframeId"]','//*[@id="noMoreToday"]')
except:
    pass


# click Class '오픈소스소프트웨어실습'
try:
    driver.switch_to.default_content()
    # 오픈소스소프트웨어실습
    # //*[@id="mCSB_1_container"]/ul/li[1]/a/span[2]/button
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    eas2 = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a/span[2]/button')
    eas2.click()
    print("오픈소스소프트웨어실습 -- 1")
except:
    pass

# click1
try:
    driver.switch_to.default_content()
    # 오픈소스소프트웨어실습 1번째 X Path
    # //*[@id="listBox"]/table/tbody/tr[1]/td[2]/div[1]/ul[3]/li/a
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    osw = driver.find_element_by_xpath('//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div[1]/ul[3]/li/a')
    name = osw.get_attribute('text') # name이 '다시보기' 버튼인지 확인하기 위함.
    print(name)
    if name != "다시보기":
        osw.click()
    else:
        # click2
        try:
            driver.switch_to.default_content()
            # 오픈소스소프트웨어실습 2번째 X Path
            # //*[@id="listBox"]/table/tbody/tr[1]/td[2]/div[2]/ul[3]/li/a
            driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
            osw = driver.find_element_by_xpath('//*[@id="listBox"]/table/tbody/tr[1]/td[2]/div[2]/ul[3]/li/a')
            osw.click()
            print("오픈소스소프트웨어실습 -- 2")
        except:
            pass

except:
    pass

# 오픈소스소프트웨어실습 참여하기 버튼 누르기
try:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="reviewForm"]')) # iframe
    eas2_1 = driver.find_element_by_xpath('//*[@id="div_virtual"]/div/ul/li[1]/a')
    eas2_1.click()
    print("오픈소스소프트웨어실습 -- 3")
except:
    pass
time.sleep(5)

# click meeting join
# try:
#     # driver.get("https://dongguk.webex.com/webappng/sites/dongguk/meeting/info/39c7ae6dcd4eb9fa55538a4a3d837966")
#     driver.switch_to.default_content()
#     # EAS2
#     eas2_1 = driver.find_element_by_xpath('//*[@id="smartJoinButton"]/span')
#     eas2_1.click()
# except:
#     pass

def button_click(img_path):
    ok = True
    t = time.time()
    while ok:
        try:
            btnLocation = pg.locateOnScreen(img_path)
            point = pg.center(btnLocation) # 화면에서 이미지와 같은 것을 찾아서 중간 좌표값 반환
            pg.click(point.x, point.y)
            ok = False
        except:
            if time.time()-t > 6:
                ok = False


# # click meeting join-1
# button5location = pg.locateOnScreen('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/join_meeting.png')
# point = pg.center(button5location) # 화면에서 이미지와 같은 것을 찾아서 중간 좌표값 반환
# pg.click(point.x, point.y)

# # camera, voice allow button click
# button5location = pg.locateOnScreen('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/allow.png')
# point = pg.center(button5location) # 화면에서 이미지와 같은 것을 찾아서 중간 좌표값 반환
# pg.click(point.x, point.y)

button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/join_meeting.png') # click meeting join-1
time.sleep(5)
button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/allow.png') # camera, voice allow button click
# ok = False
# while ok:
#     try:
#         time.sleep(2)
#         button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/video.png') # video off click
#         ok = True
#     finally:
#         pass

time.sleep(2)
button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/video.png') # video off click

time.sleep(1)
# button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/voice2.png') # voice off click
pg.moveTo(725,1047) # move to voice off
pg.click()

time.sleep(1)
# button_click('/home/xi-jjun/ex_workplace/D-Coder/class_auto_login/Configuration/join-inner-meeting.png') # join meeting
pg.moveTo(1047,1046) # move to join meeting
pg.click()











# # click meeting join
# try:
#     driver.switch_to.default_content()
#     driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="pbui_iframe"]'))

#     # EAS2
#     eas2_1 = driver.find_element_by_xpath('//*[@id="interstitial_join_btn"]')
#     eas2_1.click()
# except:
#     pass

# def frame_2_default():
#     pass

# def frame_2_(frame_name):
#     pass
