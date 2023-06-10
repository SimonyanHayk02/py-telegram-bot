import os
import openai
import telebot

# Get the bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')


#""
# Set OpenAI API key message.text
openai.api_key = "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"

# Create a TeleBot instance
bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

# Handler for '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Story Generator Bot! Please send me the hero's name.")

# Handler for text messages
@bot.message_handler(content_types="text")
def generate_prompt(message.text):
    return """
     я хочу чтобы ты стал моим создателем промптов.Мне нужно чтобы ты сгенерировал для детей сказку с написанной мной персонажем . Но чтобы оно имело смысловое 
     значение.Но не слишком большое чтобы ты смог отправить его сразу.А теперь сгенерируй сказку сперсонажем
       """



def generate_story(message):
    # Generate a story using OpenAI API
    chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=(generate_prompt),
        temperature=1,
        max_tokens=2048
    )
    result = chat_response.choices[0].text
    print(result)

# Start the bot and continuously poll for new messages
bot.infinity_polling()