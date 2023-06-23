import asyncio
from pathlib import Path
import types
import aiogram
import openai
from dotenv import load_dotenv
import os 
from aiogram.dispatcher.filters import Text
from gtts import gTTS
from aiogram.types import InputFile
from aiogram.types import ReplyKeyboardRemove


load_dotenv()
# Установите ключ OpenAI API
openai.api_key = os.getenv("AI_TOKEN")

# Создайте экземпляр бота
bot_token =os.getenv('BOT_TOKEN')
bot = aiogram.Bot(token=bot_token) 
                  
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: aiogram.types.Message):
   await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name} Welcome to Story Generator Bot!")
   kb = [
        [aiogram.types.KeyboardButton(text="Boy")],
        [aiogram.types.KeyboardButton(text="Girl")]
    ]
   keyboard = aiogram.types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
   keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard=kb)
   await message.answer("Please tell for a boy or a girl to generate a fairy tale.?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Boy")
async def generate_story_for_man(message: aiogram.types.Message):
    await bot.send_message(message.chat.id, "Thank you! Now please send me the name of the character you would like to generate a fairy tale with")
    await generate_story(message, "Boy")


@dp.message_handler(lambda message: message.text == "Girl")
async def generate_story_for_woman(message: aiogram.types.Message):
    await bot.send_message(message.chat.id, "Thank you! Now please send me the name of the character you would like to generate a fairy tale with")
    await generate_story(message, "Girl")


# Asynchronous function for generating a story
async def generate_story(message, character):
    
    await bot.send_message(message.chat.id, text="Wait, a fairy tale is being generated...")
    chat_response_final = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""I want you to be my prompt maker. I need you to generate a fairy tale for {character.lower()}
with my own character. You generate stories for {character.lower()} from 4 to 12 years old. But make sure it makes sense and isn't too big so you can send it right away.
And now generate a fairy tale with the {message.text} character.""",
        temperature=1,
        max_tokens=2048,
        top_p=1
    )
    
    print(message.text)
    result_final = chat_response_final.choices[0].text

    responce_summary = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""I want you to give me a summary of this text.{result_final}""",
        temperature=1,
        max_tokens=2048,
        top_p=1
    )
    summary = responce_summary.choices[0].text

    audio_file_path = "generated_story.mp3"
    tts = gTTS(summary)
    tts.save(audio_file_path)

    voice = InputFile(audio_file_path)
    await bot.send_voice(message.from_user.id, voice, caption="Summary of this fairy tale!")

    # Удаление временного файла
    os.remove(audio_file_path)

    # Send the generated story to the chat
    await bot.send_message(message.chat.id, f"Fairy Tale  {result_final}")

    

# Обработчик сообщений
# @dp.message_handler()
# async def handle_message(message: aiogram.types.Message):
#     # Отправляем сообщение о начале ожидания
    
#     # Асинхронно генерируем сказку
#     await generate_story(message,character)

# Запуск бота и непрерывное получение сообщений
async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())