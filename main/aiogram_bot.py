import asyncio
import aiogram
import openai
from dotenv import load_dotenv
import os 
from gtts import gTTS
from aiogram.types import InputFile 
import json



load_dotenv()
# Установите ключ OpenAI API
openai.api_key = os.getenv("AI_TOKEN")

# Создайте экземпляр бота
bot_token =os.getenv('BOT_TOKEN')
bot = aiogram.Bot(token=bot_token) 
                  
dp = aiogram.Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: aiogram.types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name} Добро пожаловать в Story Generator Bot!")
    await bot.send_message(message.from_user.id,"Пожалуйста напишите имя персонажа с которым вы бы хотели сгенерировать сказку !")
    print(message.text)
    


@dp.message_handler()
async def set_character_name(message:aiogram.types.Message):
    print(message.text,message.chat.id,message.from_user.first_name,message.from_user.last_name)
    if message.text != "Мальчик" and message.text != "Девочка":
        global user_input_text 
        user_input_text = message
        kb = [
            [
                aiogram.types.KeyboardButton(text="Мальчик"),
                aiogram.types.KeyboardButton(text="Девочка")
            ],
        ]
        keyboard = aiogram.types.ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder="Выберите способ подачи"
        )
        await message.reply("Подскажите пожалуйста для мальчика или девочки сгенерировать сказку?", reply_markup=keyboard)
    else:
        if message.text == "Мальчик":
            await generate_story(user_input_text, "Мальчик")
        elif message.text =="Девочка":
            await generate_story(user_input_text,"Девочка")
        


# Asynchronous function for generating a story
async def generate_story(message: aiogram.types.Message,gender):
            await bot.send_message(message.chat.id, text="Пожалуйста подождите пока сказка генерируется...")
            response_image = openai.Image.create(
            prompt = message["text"],
            n = 1,
            size = "256x256"
            ) 
            with open("data.json", "w") as file:
                json.dump(response_image, file,indent=4,ensure_ascii=False) 
                
                
                            
            with open("data.json", "r") as file:
                # Load the JSON data
                data = json.load(file)

            # Extract the URL from the data dictionary
            data1 = data["data"]
            url=data1[0]["url"]
           
            await bot.send_photo(message.chat.id, photo=url)

          
          
            chat_response_final = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"""Я хочу, чтобы ты был моим создателем подсказок. Мне нужно, чтобы вы создали сказку для {gender.lower()}
     с моим характером. Вы создаете истории для {gender.lower()} в возрасте от 4 до 12 лет. Но убедитесь, что оно имеет смысл и не слишком велико, чтобы вы могли отправить его прямо сейчас.
     А теперь сгенерируйте сказку с персонажем {message}.""",
            temperature=1,
            max_tokens=2048,
            top_p=1
            )
    
            print(message.text)
            result_final = chat_response_final.choices[0].text

            responce_summary = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"""Я хочу, чтобы вы кратко изложили этот текст.{result_final}""",
                temperature=1,
                max_tokens=2048,
                top_p=1
            )
            summary = responce_summary.choices[0].text

            if summary:
                audio_file_path = "generated_story.mp3"
                tts = gTTS(summary,lang="ru")
                tts.save(audio_file_path)
                voice = InputFile(audio_file_path)
                await bot.send_voice(message.from_user.id, voice, caption="Краткое содержание этой сказки!")

                # Delete the temporary audio file
                os.remove(audio_file_path)

                # Send the generated story to the chat
                await bot.send_message(message.chat.id, f"Сказка: {result_final}")
            else:
                await bot.send_message(message.chat.id, "Извините, я не смог создать действительную сказку. Пожалуйста, попробуйте еще раз.")
    


async def main():
    try: 
        await dp.start_polling()
    except Exception as e:
         print(e)
if __name__ == '__main__':
    asyncio.run(main())