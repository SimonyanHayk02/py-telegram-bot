import os
import openai
import telebot

# Get the bot token from environment variable


# Set OpenAI API key message.text
openai.api_key = "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"

# Create a TeleBot instance
bot = telebot.TeleBot("6134840576:AAE63UvD5GWK48Ls7S3afVbcJJC4jtS2snk", parse_mode=None)

# Handler for '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'],func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message, f"Hello {message.from_user.first_name} Welcome to the Story Generator Bot! Please send me the hero's name.")

# Handler for text messages
# @bot.message_handler(content_types=["text"])
@bot.message_handler(func=lambda message: True)
def generate_story(message):
    print(message.json['text'])
    # Generate a story using OpenAI API
    
    chat_response = openai.Completion.create(
        model="text-davinci-003",
        prompt="1+1",
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = chat_response.choices[0].text
    print(result)

# Start the bot and continuously poll for new messages
try:
    bot.polling()
except Exception as e:
    print(f"Error occurred during polling: {str(e)}")