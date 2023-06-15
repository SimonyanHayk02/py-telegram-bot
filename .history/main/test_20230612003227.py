from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import *
"from selenium.common.keys import Keys"

# Define the available buttons
button_list = [
    ['Button 1', 'Button 2'],
    ['Button 3', 'Button 4']
]

def start(bot, update):
    # Create a ReplyKeyboardMarkup object with the button list
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True)
    
    # Send the message with buttons
    bot.send_message(chat_id=update.message.chat_id, text='Choose an option:', reply_markup=reply_markup)

def button_handler(bot, update):
    # Get the selected button text
    selected_button = update.message.text
    
    # Handle the selected button
    if selected_button == 'Button 1':
        bot.send_message(chat_id=update.message.chat_id, text='You pressed Button 1!')
    elif selected_button == 'Button 2':
        bot.send_message(chat_id=update.message.chat_id, text='You pressed Button 2!')
    elif selected_button == 'Button 3':
        bot.send_message(chat_id=update.message.chat_id, text='You pressed Button 3!')
    elif selected_button == 'Button 4':
        bot.send_message(chat_id=update.message.chat_id, text='You pressed Button 4!')

async def start_commmand(update, context):
    await update.message.reply_text('Hello! Welcome To Store!')

if __name__ == '__main__':
    application = Application.builder().token(keys.token).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))

    # Run bot
    application.run_polling(1.0)