from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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

def main():
    # Set up the Telegram bot
    updater = Updater(bot)
    dp = updater.dispatcher

    # Set up handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, button_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()