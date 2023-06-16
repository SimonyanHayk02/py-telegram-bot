import openai
import telebot
import threading
import asy



# Get the bot token from environment variable


# Set OpenAI API key message.text
openai.api_key = "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"

# Create a TeleBot instance
bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

# Handler for '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'],func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name} Welcome to the Story Generator Bot! Please send me the hero's name.")
    loading_message = bot.reply_to(message, "Загрузка...")

    # Запускаем поток для генерации сказки
    generate_thread = threading.Thread(target=generate_story, args=(message,))
    generate_thread.start()

    # Ожидаем завершения потока и удаляем сообщение с индикатором загрузки
    generate_thread.join()
    bot.delete_message(message.chat.id, loading_message.message_id)

# Handler for text messages

@bot.message_handler(func=lambda message: True)
async def generate_story(message):
    # Generate a story using OpenAI API
    chat_response =  openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""Я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку
    с написанной мной персонажем.Ты генерируешь сказки для детей от 4 до 12 лет.Но чтобы оно имело смысловое значение.Но не слишком большое чтобы ты смог отправить его сразу.
    Но ты должен проверить етих персонажей из фильмов, мултьтфильмов,сказок,знаменитых игр и так далее чтобы я знал сушествует ли такой персонаж на самом деле.
    А теперь сгенерируй сказку с персонажем {message.json['text']} .Но перед тем как сказать тебе етого персонажа мне нужно чтобы ты проверил сушествует ли такой персонаж или нет если сушествует то ты должен
    дать мне сгенерированну сказку а если нет просто скажу что такого персонажа не сушествует и все не надо добавлять другие слова""",
        temperature=1,
        max_tokens=2048,
        top_p=1
    )
    result = chat_response.choices[0].text
    bot.reply_to(message, f"{result}")
    await bot.reply_to(message, "Подождите, идет генерация сказки...")

# Start the bot and continuously poll for new messages
try:
    bot.polling()
except Exception as e:
    print(f"Error occurred during polling: {str(e)}")