# 재미로 만든 동국대학교 학식 봇  
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
cmd_manual = "/help : 사용방법을 알려드립니다!\n\n[오늘]\n/s11 : 오늘 상록원1층식당(솥앤누들)\n/s12 : 오늘 상록원1층식당(솥앤누들) Take Out\n/s3 : 오늘 상록원3층식당 중식\n/nu1 : 오늘 누리터 식당(일산캠퍼스) 누리밥상 중식\n/nu2 : 오늘 누리터 식당(일산캠퍼스) 더진국\n\n[월~금]\n/ss1 : 월~금 상록원1층식당(솥앤누들)\n/ss12 : 월~금 상록원1층식당(솥앤누들) Take Out\n/ss3 : 월~금 상록원3층식당\n/nuri1 : 월~금 누리터 식당(일산캠퍼스) - 누리밥상\n/nuri2 : 월~금 누리터 식당(일산캠퍼스) - 더진국"


# telegram token
my_token = 'TELEGRAM TOKEN' # dgufood_bot 

print('start telegram chat bot')


def get_titles(res):
    pass

url = 'https://dgucoop.dongguk.edu:44649/store/store.php?w=4&l=2'

response = requests.get(url)
html = response.content.decode('euc-kr', 'replace')
dgu_soup = BeautifulSoup(html, 'html.parser')

# sang Rock Won 3th floor , sang Rock Won first floor , 1 san
food_restaurant = [] 
foods = []


# title of restaurants....
food_title1 = dgu_soup.find("table", {"border":"0"})
food_title2 = food_title1.find_all("td", {"colspan":"9"})

for i in food_title2:
    food_restaurant.append(i.get_text())
# ....title of restaurants


# foods [0]~[6] : SUN ~ SAT
food1 = dgu_soup.find("table", {"border":"0"})
food2 = food1.find_all('span',{"style":"color:#303030;font-size:9pt;"})

for i in food2:
    foods.append(i.get_text())


manual = "동국대학교 학식 알림봇에 오신 것을 환영합니다!! /help 로 서비스를 이용해보세요!!"

'''
# sang Rock won 3th floor lunch[house bab]
print(foods[1],"\n") # Mon
print(foods[2],"\n") # Tue
print(foods[3],"\n") # Wed
print(foods[4],"\n") # Thu
print(foods[5],"\n") # Fri

# sang Rock won 3th floor dinner
# NOT UPDATED YET
print(foods[1],"\n") # Mon
print(foods[2],"\n") # Tue
print(foods[3],"\n") # Wed
print(foods[4],"\n") # Thu
print(foods[5],"\n") # Fri

# sang Rock won first floor
print(foods[22],"\n") # Mon
print(foods[23],"\n") # Tue
print(foods[24],"\n") # Wed
print(foods[25],"\n") # Thu
print(foods[26],"\n") # Fri

# Take Out sang Rock won first floor
print(foods[29],"\n") # Mon
print(foods[30],"\n") # Tue
print(foods[31],"\n") # Wed
print(foods[32],"\n") # Thu
print(foods[33],"\n") # Fri

# Nuritar (ill san CAMPUS) - Nuri bab sang
print(foods[78],"\n") # Mon
print(foods[79],"\n") # Tue
print(foods[80],"\n") # Wed
print(foods[81],"\n") # Thu
print(foods[82],"\n") # Fri

# Nuritar (ill san CAMPUS) - The Jin soup
print(foods[85],"\n") # Mon
print(foods[86],"\n") # Tue
print(foods[87],"\n") # Wed
print(foods[88],"\n") # Thu
print(foods[89],"\n") # Fri
'''

def time_check():
    # Sun Mar 21 15:09:59 2021
    time_now = time.strftime('%c', time.localtime(time.time()))
    day_now = time_now[:3]
    return day_now

def daily_food(day):
    pass

def reply_start(update, context):
    #global food_restaurant
    if update.message.text == "점심" or update.message.text == "밥" or update.message.text == "시작" or update.message.text == "start" or update.message.text == "help" or update.message.text != ".":
        update.message.reply_text(manual)
        

# message reply function
def get_message(update, context):

    if update.message.text == "Hi" or update.message.text == "안녕" or update.message.text == "ㅎㅇ" or update.message.text != ".":
        update.message.reply_text("반가워요!! 저는 동국대학교 학식 봇입니다. 학식이 궁금하시면 /help를 입력해주세요!")

    """if update.message.text == today_lunch:
        #update.message.reply_text(food_restaurant[0]+"\n"+food_restaurant[1]+"\n"+food_restaurant[2])
        if time_check() == "Mon":
            update.message.reply_text(foods[1])
        elif time_check() == "Tue":
            update.message.reply_text(foods[2])
        elif time_check() == "Wed":
            update.message.reply_text(foods[3])
        elif time_check() == "Thu":
            update.message.reply_text(foods[4])
        elif time_check() == "Fri":
            update.message.reply_text(foods[5])
        elif time_check() == "Sun":
            try:
                update.message.reply_text(foods[0])
            except:
                update.message.reply_text("No Food :( ")
        elif time_check() == "Sat":
            try:
                update.message.reply_text(foods[6])
            except:
                update.message.reply_text("No Food :( ")"""

# help reply function | command handler
def help_command(update, context) :
    update.message.reply_text("무엇을 도와드릴까요?")
    update.message.reply_text(cmd_manual)

def sang3_command(update, context):
    update.message.reply_text("상록원3층식당\n\n"+"[월요일]\n"+foods[1]+"\n\n"+"[화요일]\n"+foods[2]+"\n\n"+"[수요일]\n"+foods[3]+"\n"+"[목요일]\n"+foods[4]+"\n\n"+"[금요일]\n"+foods[5])

def sang1_command(update, context):
    update.message.reply_text("상록원1층식당\n\n"+"[월요일]\n"+foods[22]+"\n\n"+"[화요일]\n"+foods[23]+"\n\n"+"[수요일]\n"+foods[24]+"\n\n"+"[목요일]\n"+foods[25]+"\n\n"+"[금요일]\n"+foods[26])

def sang1take_command(update, context):
    update.message.reply_text("상록원1층식당 Take Out\n\n"+"[월요일]\n"+foods[29]+"\n\n"+"[화요일]\n"+foods[30]+"\n\n"+"[수요일]\n"+foods[31]+"\n\n"+"[목요일]\n"+foods[32]+"\n\n"+"[금요일]\n"+foods[33])

def nuri1_command(update, context):
    update.message.reply_text("누리터 식당(일산캠퍼스) - 누리밥상 중식\n\n"+"[월요일]\n"+foods[78]+"\n\n"+"[화요일]\n"+foods[79]+"\n\n"+"[수요일]\n"+foods[80]+"\n\n"+"[목요일]\n"+foods[81]+"\n\n"+"[금요일]\n"+foods[82])

def nuri2_command(update, context):
    update.message.reply_text("누리터 식당(일산캠퍼스) - 더진국\n\n"+"[월요일]\n"+foods[85]+"\n\n"+"[화요일]\n"+foods[86]+"\n\n"+"[수요일]\n"+foods[87]+"\n\n"+"[목요일]\n"+foods[88]+"\n\n"+"[금요일]\n"+foods[89])

def s1_1_command(update, context) :
    update.message.reply_text("상록원1층식당(솥앤누들)")
    if time_check() == "Mon":
        update.message.reply_text(foods[22])
    elif time_check() == "Tue":
        update.message.reply_text(foods[23])
    elif time_check() == "Wed":
        update.message.reply_text(foods[24])
    elif time_check() == "Thu":
        update.message.reply_text(foods[25])
    elif time_check() == "Fri":
        update.message.reply_text(foods[26])
    elif time_check() == "Sun":
        try:
            update.message.reply_text(foods[21])
        except:
            update.message.reply_text("No Food :( ")
    elif time_check() == "Sat":
        try:
            update.message.reply_text(foods[27])
        except:
            update.message.reply_text("No Food :( ")

def s1_2_command(update, context) :
    update.message.reply_text("상록원1층식당(솥앤누들) Take Out")
    if time_check() == "Mon":
        update.message.reply_text(foods[29])
    elif time_check() == "Tue":
        update.message.reply_text(foods[30])
    elif time_check() == "Wed":
        update.message.reply_text(foods[31])
    elif time_check() == "Thu":
        update.message.reply_text(foods[32])
    elif time_check() == "Fri":
        update.message.reply_text(foods[33])
    elif time_check() == "Sun":
        try:
            update.message.reply_text(foods[28])
        except:
            update.message.reply_text("No Food :( ")
    elif time_check() == "Sat":
        try:
            update.message.reply_text(foods[34])
        except:
            update.message.reply_text("No Food :( ")

def s3_command(update, context) :
    update.message.reply_text("상록원3층식당 중식")
    if time_check() == "Mon":
        update.message.reply_text(foods[1])
    elif time_check() == "Tue":
        update.message.reply_text(foods[2])
    elif time_check() == "Wed":
        update.message.reply_text(foods[3])
    elif time_check() == "Thu":
        update.message.reply_text(foods[4])
    elif time_check() == "Fri":
        update.message.reply_text(foods[5])
    elif time_check() == "Sun":
        try:
            update.message.reply_text(foods[0])
        except:
            update.message.reply_text("No Food :( ")
    elif time_check() == "Sat":
        try:
            update.message.reply_text(foods[6])
        except:
            update.message.reply_text("No Food :( ")

def nu_1_command(update, context) :
    update.message.reply_text("누리터 식당(일산캠퍼스) 누리밥상 중식")
    if time_check() == "Mon":
        update.message.reply_text(foods[78])
    elif time_check() == "Tue":
        update.message.reply_text(foods[79])
    elif time_check() == "Wed":
        update.message.reply_text(foods[80])
    elif time_check() == "Thu":
        update.message.reply_text(foods[81])
    elif time_check() == "Fri":
        update.message.reply_text(foods[82])
    elif time_check() == "Sun":
        try:
            update.message.reply_text(foods[77])
        except:
            update.message.reply_text("No Food :( ")
    elif time_check() == "Sat":
        try:
            update.message.reply_text(foods[83])
        except:
            update.message.reply_text("No Food :( ")

def nu_2_command(update, context) :
    update.message.reply_text("누리터 식당(일산캠퍼스) 더진국")
    if time_check() == "Mon":
        update.message.reply_text(foods[85])
    elif time_check() == "Tue":
        update.message.reply_text(foods[86])
    elif time_check() == "Wed":
        update.message.reply_text(foods[87])
    elif time_check() == "Thu":
        update.message.reply_text(foods[88])
    elif time_check() == "Fri":
        update.message.reply_text(foods[89])
    elif time_check() == "Sun":
        try:
            update.message.reply_text(foods[84])
        except:
            update.message.reply_text("No Food :( ")
    elif time_check() == "Sat":
        try:
            update.message.reply_text(foods[90])
        except:
            update.message.reply_text("No Food :( ")

def start_command(update, context) :
    update.message.reply_text("Welcome!!")

# Command Handler function
def Command_Handler(cmd,func):
    handler = CommandHandler(cmd,func)
    updater.dispatcher.add_handler(handler)

updater = Updater(my_token, use_context=True) # take updates of bot
"""
reply_handler = MessageHandler(Filters.text & (~Filters.command), reply_start) # call get_messate function
updater.dispatcher.add_handler(reply_handler) # add handler
"""
message_handler = MessageHandler(Filters.text & (~Filters.command), get_message) # call get_messate function
updater.dispatcher.add_handler(message_handler) # add handler


# function
Command_Handler(help_cmd, help_command)     # /help
Command_Handler("s11", s1_1_command)        # /s11 : s
Command_Handler("s12", s1_2_command)        # /s12
Command_Handler("s3", s3_command)           # /s3
Command_Handler("nu1", nu_1_command)        # /nu1
Command_Handler("nu2", nu_2_command)        # /nu2
Command_Handler("nuri1", nuri1_command)     # /nuri1 : 1san all
Command_Handler("nuri2", nuri2_command)     # /nuri2 : 1san all
Command_Handler("ss3", sang3_command)       # /ss3 : sang 3th all
Command_Handler("ss1", sang1_command)       # /ss1 : sang first all
Command_Handler("ss12", sang1take_command)  # /ss12 : sang first take out all
Command_Handler(start, start_command)


updater.start_polling(timeout=3, clean=True)
updater.idle()
