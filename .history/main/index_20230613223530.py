import os
import openai
import telebot 
from telebot import types

# BOT_TOKEN = os.getenv('BOT_TOKEN')


openai.api_key = "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"


bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Hello {message.chat.id} welcome to the Story Generator Bot! Please send me the hero's name.")
    

@bot.message_handler(func=lambda message: True)
def generate_story(message):
    # Generate a story using OpenAI API
    chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
        Я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку
    с написанной мной персонажем.Ты генерируешь сказки для детей от 4 до 12 лет.Но чтобы оно имело смысловое значение.Но не слишком большое чтобы ты смог отправить его сразу.
    Но ты должен проверить етих персонажей из фильмов, мултьтфильмов,сказок,знаменитых игр и так далее чтобы я знал сушествует ли такой персонаж на самом деле.
    А теперь сгенерируй сказку с персонажем  .Но перед тем как сказать тебе етого персонажа мне нужно чтобы ты проверил сушествует ли такой персонаж или нет если сушествует то ты должен
    дать мне сгенерированну сказку а если нет сказать что такого персонажа не сушествует.
     """ ,
        temperature=1,
        max_tokens=2048
    )
    first_response = chat_response.choices[0].text
    bot.send_message(message.chat.id, first_response)

        
bot.infinity_polling()