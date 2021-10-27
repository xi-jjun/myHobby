# 학교 홈페이지 자동으로 들어가서 수업 자동으로 들어가주는 프로그램
import pyautogui
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

path = "/home/xi_jjun/workspace/D-Coder/class_auto_login/chromedriver"
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

    login_ID = '2016'
    login_PW = ''

    elem = driver.find_element_by_xpath('//*[@id="id"]')
    elem.send_keys(login_ID)
    elem = driver.find_element_by_name("userDTO.password")
    elem.send_keys(login_PW)

    elem.send_keys(Keys.RETURN) # Enter Kry
except:
    pass

# kill popup
try:
    killPopUp('/html/frameset/frame','//*[@id="modalIframeId"]','//*[@id="noMoreToday"]')
except:
    pass

# click EAS2 classIN button in main frame
try:
    driver.switch_to.default_content()
    # EAS2
    # //*[@id="mCSB_1_container"]/ul/li[1]/a/span[2]/button 
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    eas2 = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a/span[2]/button')
    eas2.click()
    print("EAS2 -- 1")
except:
    pass

# click
try:
    driver.switch_to.default_content()
    # EAS2
    # //*[@id="mCSB_1_container"]/ul/li[1]/a/span[2]/button # EAS2-1
    #//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div[1]/ul[3]/li/a # EAS2-2
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    eas2_1 = driver.find_element_by_xpath('//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div[1]/ul[3]/li/a')
    eas2_1.click()
    print("EAS2 -- 2")
except:
    pass

try:
    driver.switch_to.default_content()
    # EAS2
    # //*[@id="mCSB_1_container"]/ul/li[1]/a/span[2]/button # EAS2-1
    #//*[@id="listBox"]/table/tbody/tr[1]/td[1]/div[1]/ul[3]/li/a # EAS2-2
    driver.switch_to.frame(driver.find_element_by_xpath('/html/frameset/frame'))
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="reviewForm"]')) # iframe
    eas2_1 = driver.find_element_by_xpath('//*[@id="div_virtual"]/div/ul/li[1]/a')
    eas2_1.click()
    print("EAS2 -- 3")
except:
    pass
time.sleep(5)
# click meeting join
try:
    driver.switch_to.default_content()
    # EAS2
    eas2_1 = driver.find_element_by_xpath('//*[@id="smartJoinButton"]')
    eas2_1.click()
except:
    pass


# click meeting join
try:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="pbui_iframe"]'))
    
    # EAS2
    eas2_1 = driver.find_element_by_xpath('//*[@id="interstitial_join_btn"]')
    eas2_1.click()
except:
    pass

def frame_2_default():
    pass

def frame_2_(frame_name):
    pass

