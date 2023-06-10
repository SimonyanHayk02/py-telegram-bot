import os

import telebot

from telebot.types import Message

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def echo(message : Message):
  BOT_TOKEN.reply_to(message = message, text="sample")
    
bot.infinity_poling()