import os
import openai
import telebot


BOT_TOKEN = os.getenv('BOT_TOKEN')
openai.api_key = "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"

bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk",parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Story Generator Bot! Please send me the hero's name.")

@bot.message_handler(content_types="text")
def generate_story(message):
   chat_response = openai.Completion.create(
   model="text-davinci-003",
   prompt=message.text,
   temperature=1,
   max_tokens= 2048
)
   result = chat_response.choices[0].text
   print(result)
   
# Start the bot
bot.infinity_polling()




