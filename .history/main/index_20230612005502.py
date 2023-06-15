import os
import openai
import telebot 
from telebot import types

# Get the bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Set OpenAI API key message.text
openai.api_key = "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"

# Create a TeleBot instance
bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

# Handler for '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    username =message.from_user.username
    bot.send_message(username, f"Hello {username} welcome to the Story Generator Bot! Please send me the hero's name.")
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button_1 = types.KeyboardButton('Button 1')
    button_2 = types.KeyboardButton('Button 2')
    keyboard.add(button_1,button_2)
    bot.send_message(message.chat.id,"Choose an option", reply_markup=keyboard)

# Handler for text messages


def generate_story(message):
    # Generate a story using OpenAI API
#     chat_response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"""
#      я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку
#      с написанной мной персонажем.Но чтобы оно имело смысловое значение.Но не слишком большое чтобы ты смог отправить его сразу.И мне не нужны обзацы чтобы не потерять слов. Например сказка про соника.
#      Соник, маленький и быстрый ежик, жил в волшебном лесу по имени Зеленая Роща. У него были ярко-синие шипы и пронзительные синие глаза. Соник был известен своей невероятной скоростью, и никто не мог его поймать.
#   Однажды в Зеленой Роще произошло страшное событие. Злой доктор Роботник решил захватить лес и заполонить его механическими созданиями. Жители леса были в опасности, и им требовалась помощь.
#   Слыша о беде, Соник собрал всю свою смелость и решимость. Он отправился в путь, пробегая по полям и лесам, чтобы остановить доктора Роботника и его зловещие планы. С каждым шагом он становился быстрее и сильнее.
#   По пути Соник встретил разных животных, которые нуждались в его помощи. Он помог утке найти своих утят, спас заблудшего зайчонка и защитил рыбок в реке от опасных хищников. Все они благодарили Соника за его отвагу и доброту.
#   Наконец, Соник добрался до замка доктора Роботника. Там его ждали множество ловушек и роботов, но Соник не смутился. Он использовал свою скорость и ловкость, чтобы преодолеть все препятствия и разрушить механическую армию доктора Роботника.
#   После долгой и тяжелой битвы, Соник победил злодея и освободил Зеленую Рощу от его зловещего влияния. Жители леса были благодарны Сонику за его храбрость и спасение.
#   Соник вернулся в Зеленую Рощу, где был приветствован как настоящий герой. Он продолжал защищать свой любимый лес и помогать тем, кто в нем нуждался.

#     А теперь мне нужно чтобы ты сгенерировал мне сказку с етим персонажем 
#           {message.text}      """ ,
#         temperature=1,
#         max_tokens=2048
#     )
#     result = chat_response.choices[0].text
#     print(result)
    if message.text == 'Button 1':
        bot.send_message(message.chat.id, "Button 1 pressed")
        # Perform action for Button 1
    elif message.text == 'Button 2':
        bot.send_message(message.chat.id, "Button 2 pressed")
        # Perform action for Button 2

# Start the bot and continuously poll for new messages
bot.infinity_polling()