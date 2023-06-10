import os
import openai
import telebot


BOT_TOKEN = os.getenv('BOT_TOKEN')
openai.api_key = os.getenv("AI_TOKEN")


bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk",parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Story Generator Bot! Please send me the hero's name.")

@bot.message_handler(func=lambda message: True)
def generate_story(message):
     message.text.strip()
    print(message) 


# Start the bot
bot.infinity_polling()



# @bot.message_handler(commands=['start'])
# def echo(message : Message):
#   BOT_TOKEN.reply_to(message = message, text="sample")

# bot.polling()

