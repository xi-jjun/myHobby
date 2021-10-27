# Test Code
import telegram  
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules

# Command Handler Constant
help_cmd = 'help'
start = 'start'
today_breakfast = 'breakfast'
today_lunch = 'lunch'
today_dinner = 'dinner'

total_cmd = [help_cmd,start,today_breakfast,today_lunch,today_dinner]


# telegram token
my_token = 'TETEGRAM TOKEN' # dgufood_bot 

print('start telegram chat bot')

# message reply function
def get_message(update, context):
    #update.message.reply_text("got text")
    update.message.reply_text(update.message.text)

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
