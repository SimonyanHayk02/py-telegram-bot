import os

import telebot

from telebot.types import Message

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def echo(message : Message):
  bot_client.reply_to
bot.infinity_poling()