import asyncio
import aiogram
import openai
from dotenv import load_dotenv
import os 


load_dotenv()
# Установите ключ OpenAI API
openai.api_key = os.getenv("AI_TOKEN")



# Создайте экземпляр бота
bot_token =os.getenv('BOT_TOKEN')
bot = aiogram.Bot(token=bot_token) 
                  
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.username} Welcome to the Story Generator Bot! Please send me the hero's name.")
   
# Асинхронная функция для генерации сказки
async def generate_story(message):
    # Генерация сказки с использованием OpenAI API
    chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""Я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку
    с написанной мной персонажем.Ты генерируешь сказки для детей от 4 до 12 лет.Но чтобы оно имело смысловое значение.Но не слишком большое чтобы ты смог отправить его сразу.
    Но ты должен проверить етих персонажей из фильмов, мултьтфильмов,сказок,знаменитых игр и так далее чтобы я знал сушествует ли такой персонаж на самом деле.
    А теперь сгенерируй сказку с персонажем {message.text} .Но перед тем как сказать тебе етого персонажа мне нужно чтобы ты проверил сушествует ли такой персонаж или нет если сушествует то ты должен
    дать мне сгенерированну сказку а если нет просто скажу что такого персонажа не сушествует и все не надо никакого обьяснения""",
        temperature=1,
        max_tokens=2048,
        top_p=1
    )
    result = chat_response.choices[0].text

    # Отправка сгенерированной сказки в чат
    await bot.send_message(message.chat.id, f"Сказка {result}")

# Обработчик сообщений
@dp.message_handler()
async def handle_message(message: aiogram.types.Message):
    # Отправляем сообщение о начале ожидания
    await bot.send_message(chat_id=message.chat.id, text="Подождите, идет генерация сказки...")
    # Асинхронно генерируем сказку
    await generate_story(message)

# Запуск бота и непрерывное получение сообщений
async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())