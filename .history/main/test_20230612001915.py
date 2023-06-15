from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Define the available buttons
button_list = [
    ['Button 1', 'Button 2'],
    ['Button 3', 'Button 4']
]

def start(update, context):
    # Create a ReplyKeyboardMarkup object with the button list
    reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard=True)
    
    # Send the message with buttons
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)

def button_handler(update, context):
    # Get the selected button text
    selected_button = update.message.text
    
    # Handle the selected button
    if selected_button == 'Button 1':
        update.message.reply_text('You pressed Button 1!')
    elif selected_button == 'Button 2':
        update.message.reply_text('You pressed Button 2!')
    elif selected_button == 'Button 3':
        update.message.reply_text('You pressed Button 3!')
    elif selected_button == 'Button 4':
        update.message.reply_text('You pressed Button 4!')

def main():
    # Set up the Telegram bot
    updater = Updater('6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk', use_context=True)
    dp = updater.dispatcher

    # Set up handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, button_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()