# 학교 홈페이지 자동 로그인 Pyautogui 버전.
import pyautogui
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from pyvirtualdisplay import Display 
import time

exit_button_img = r'/home/xi_jjun/workspace/D-Coder/class_auto_login/Configuration/exit_button2.png'
login_img = r'/home/xi_jjun/workspace/D-Coder/class_auto_login/Configuration/login_button.png'
id_entry_img = r'/home/xi_jjun/workspace/D-Coder/class_auto_login/Configuration/id_entry.png'
password_entry_img = r'/home/xi_jjun/workspace/D-Coder/class_auto_login/Configuration/pw_entry.png'


path = "/home/xi_jjun/workspace/D-Coder/class_auto_login/chromedriver"
driver = webdriver.Chrome(path)
driver.set_window_size(1600,1080)
driver.implicitly_wait(10)
driver.get("https://eclass.dongguk.edu/") # web page load

time.sleep(2)

# kill popup window
exit_button = pyautogui.locateCenterOnScreen(exit_button_img)
pyautogui.click(exit_button)

time.sleep(1)

# click login button
login_button = pyautogui.locateCenterOnScreen(login_img)
pyautogui.click(login_button)

time.sleep(0.5)

# click login entry
login_entry = pyautogui.locateCenterOnScreen(id_entry_img)
pyautogui.click(login_entry)

time.sleep(0.5)

# insert my ID 2016111952
pyautogui.press('2')
pyautogui.press('0')
pyautogui.press('1')
pyautogui.press('6')


# click password entry
password_entry = pyautogui.locateCenterOnScreen(password_entry_img)
pyautogui.click(password_entry)

time.sleep(0.5)

# insert my Password
pyautogui.press('1')
pyautogui.press('2')
pyautogui.press('3')
pyautogui.press('4')
pyautogui.press('5')
pyautogui.press('6')

time.sleep(0.5)

# click enter
pyautogui.press('enter')


time.sleep(2)

lmain = driver.find_element_by_xpath('//*[@id="mainContent"]/form/div/div[4]/ul/li[1]/a/span')
lmain.click()

"""
login_ID = '2016'
login_PW = ''

elem = driver.find_element_by_name("userDTO.userid")
elem.send_keys(login_ID)
elem = driver.find_element_by_name("userDTO.password")
elem.send_keys(login_PW)

elem.send_keys(Keys.RETURN) # Enter Kry
"""