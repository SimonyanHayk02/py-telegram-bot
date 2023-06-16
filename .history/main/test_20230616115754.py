import asyncio
import aiogram
import openai

# Установите ключ OpenAI API
openai.api_key = "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"

# Создайте экземпляр бота
bot = aiogram.Bot(token="6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk")
dp = aiogram.Dispatcher(bot)

@bot.message_handler(commands=['start', 'help'],func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name} Welcome to the Story Generator Bot! Please send me the hero's name.")
   

# Асинхронная функция для генерации сказки
async def generate_story(message):
    # Генерация сказки с использованием OpenAI API
    chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Сказка с персонажем: {message.text}",
        temperature=1,
        max_tokens=2048,
        top_p=1
    )
    result = chat_response.choices[0].text

    # Отправка сгенерированной сказки в чат
    await bot.send_message(chat_id=message.chat.id, text=result)

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