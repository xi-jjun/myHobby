import telegram
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Command Handler Constant
help_cmd = 'help'
start = 'start'
today_breakfast = 'breakfast'
today_lunch = 'lunch'
today_dinner = 'dinner'

total_cmd = [help_cmd,start,today_breakfast,today_lunch,today_dinner]

# telegram token
my_token = 'TELEGRAM TOKEN' # dgufood_bot 

print('start telegram chat bot')


# dongguk unvi 
request = requests.get("http://seoul.jbdream.or.kr/bbs/board.php?bo_table=sub03_02%22")

html = request.text

# HTML 소스코드를 파이썬 객체로 변환합니다.
soup = BeautifulSoup(html, 'html.parser')

# <td> 태그를 포함하는 요소를 추출
# tr = soup.select(' tr> td')

# menu = str(soup.find_all('td' , {'class' : 'td_board1'}))

menu = soup.select("td.td_board1")

month_date = soup.select("td.td_num")

# 날짜 설정
date_list = []
for dat in month_date:
        date_list.append(dat.text)

year = (datetime.today().strftime('%Y'))
month = int(datetime.today().strftime('%m'))
day = int(datetime.today().strftime('%d'))
print(year, month, day)

def getDay():
    now = time.localtime()
    daylist = ['월', '화', '수', '목', '금', '토', '일']
    return daylist[now.tm_wday]

ccc = getDay()


# 메뉴 설정
menu_list = []
for bap in menu:
    menu_list.append(bap.text)

for i in range(6):
    if ccc == date_list[i]:
        print(f"오늘은  {date_list[i]}요일 입니다")

        if i == 0: # MON
            print(menu_list[0])
        elif i == 1:
            print(menu_list[3:6])
        elif i == 2:
            print(menu_list[6:9])
        elif i == 3:
            print(menu_list[9:12] )
        elif i == 4:
            print(menu_list[12:15])
        elif i == 5:
            print(menu_list[15:18]) # breakfast , lunch , dinner
        elif i == 6:
            print(menu_list[18:21])




# message reply function
def get_message(update, context):
    #update.message.reply_text("got text")
    update.message.reply_text(update.message.text)
    if update.message.text == today_breakfast:
        update.message.reply_text(menu_list[15])

# help reply function | command handler
def help_command(update, context) :
    update.message.reply_text("무엇을 도와드릴까요?")
    for cmd in total_cmd:
        update.message.reply_text(cmd)


def start_command(update, context) :
    update.message.reply_text("Welcome!!")

# Command Handler function
def Command_Handler(cmd,func):
    handler = CommandHandler(cmd,func)
    updater.dispatcher.add_handler(handler)


updater = Updater(my_token, use_context=True) # take updates of bot

message_handler = MessageHandler(Filters.text & (~Filters.command), get_message) # call get_messate function
updater.dispatcher.add_handler(message_handler) # add handler

Command_Handler(help_cmd, help_command)
Command_Handler(start, start_command)


updater.start_polling(timeout=3, clean=True)
updater.idle()