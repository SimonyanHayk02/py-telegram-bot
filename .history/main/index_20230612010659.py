import os
import openai
import telebot 
from telebot import types

# BOT_TOKEN = os.getenv('BOT_TOKEN')


openai.api_key = "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"


bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
   # user_first_name = message.chat.id

    bot.send_message(message.chat.id, f"Hello {message.chat.id} welcome to the Story Generator Bot! Please send me the hero's name.")
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton('Button 1')
    button_2 = types.KeyboardButton('Button 2')
    keyboard.add(button_1,button_2)
    bot.send_message(message.chat.id,"Choose an option", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def generate_story(message):
    # Generate a story using OpenAI API

    if message.text == 'Button 1':
        bot.send_message(message.chat.id, "Button 1 pressed")
      
    elif message.text == 'Button 2':
        bot.send_message(message.chat.id, "Button 2 pressed")
        
bot.infinity_polling()