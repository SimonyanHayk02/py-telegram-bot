import os
import openai
import telebot
from telebot.types import Message

BOT_TOKEN = os.environ.get('BOT_TOKEN')
openai.api_key = os.getenv("AI_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="# Python 3 \ndef remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn x \n\n# Explanation of what the code does\n\n#",
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)



# @bot.message_handler(commands=['start'])
# def echo(message : Message):
#   BOT_TOKEN.reply_to(message = message, text="sample")

# bot.polling()

