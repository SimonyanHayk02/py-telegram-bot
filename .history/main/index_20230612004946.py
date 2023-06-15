import os
import telebot 
from telebot import types
import openai

# Get the bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Create a TeleBot instance
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

# Handler for '/start' command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.chat.id
    bot.send_message(username, f"Hello {username}! Welcome to the Story Generator Bot.")
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton('Button 1')
    button_2 = types.KeyboardButton('Button 2')
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)

# Handler for button clicks
@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    if message.text == 'Button 1':
        bot.send_message(message.chat.id, "Button 1 pressed")
        # Perform action for Button 1
    elif message.text == 'Button 2':
        bot.send_message(message.chat.id, "Button 2 pressed")
        # Perform action for Button 2

# Start the bot and continuously poll for new messages
bot.infinity_polling()