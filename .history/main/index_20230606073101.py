import os

import telebot

from telebot.types import types

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def echo(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()