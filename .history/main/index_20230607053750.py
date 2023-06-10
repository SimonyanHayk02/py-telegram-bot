import os
import openai
import telebot
from telebot.types import Message


BOT_TOKEN = os.environ.get('BOT_TOKEN')
openai.api_key = os.getenv("AI_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN")
openai.organization = "org-XGzTVxCddVxXANcR0iMCugR5"
openai.Model.list()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Story Generator Bot! Please send me the hero's name.")

@bot.message_handler(func=lambda message: True)
def generate_story(message):
    name = message.text.strip()

    if not name:
        bot.reply_to(message, "Please provide a valid hero's name.")
        return

    prompt = f"Once upon a time, there was a hero named {name}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
    )
    story = response.choices[0].text.strip().replace(prompt, "")

    bot.reply_to(message, story)

# Start the bot
bot.polling()



# @bot.message_handler(commands=['start'])
# def echo(message : Message):
#   BOT_TOKEN.reply_to(message = message, text="sample")

# bot.polling()

