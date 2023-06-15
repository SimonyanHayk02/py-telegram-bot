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
    button_1 = types.KeyboardButton('Mario')
    button_2 = types.KeyboardButton('Button 2')
    keyboard.add(button_1,button_2)
    bot.send_message(message.chat.id,"Choose an option", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def generate_story(message):
    # Generate a story using OpenAI API
    chat_response = None
    if message.text == 'Mario':
        chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
     я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку
     с написанной мной персонажем.Но чтобы оно имело смысловое значение.Но не слишком большое чтобы ты смог отправить его сразу.И мне не нужны обзацы чтобы не потерять слов.
    Но перед тем как сказать тебе етого персонажа мне нужно чтобы ты проверил сушествует ли такой персонаж или нет если сушествует то ты должен
    дать мне сгенерированну сказку а если нет сказать что такого персонажа не сушествует.
      Но ты должен проверить етих персонажей из фильмов, мултьтфильмов,сказок,знаменитых игр и так далее.Ты генерируешь сказки для детей от 4 до 12 лет.А теперь сгенерируй сказку сперсонажем Саб Зиро.Мне нужно чтобы у сказки было смысловое начало и окончание.

                """ ,
        temperature=1,
        max_tokens=2048
    )
    first_response = chat_response.choices[0].text
    bot.send_message(message.chat.id, first_response)

        
bot.infinity_polling()