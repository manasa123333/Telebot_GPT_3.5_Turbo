from aiogram import Bot, Dispatcher,executor,types
from dotenv import load_dotenv
import os
import openai
import sys

class Reference:
    '''
    A class to store previous response from the chatgpt api
    '''

    def __init__(self) -> None:
        self.response = ""

load_dotenv()
openai.api_key = os.getenv('OpenAI_API_KEY')

reference = Reference()

API_TOKEN = os.getenv('TOKEN')

MODEL_NAME = "gpt-3.5-turbo"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def clear_past():
    reference.response = ""

@dp.message_handler(commands=['start'])
async def Welcome(message: types.Message):
    """
    This handler receives messages with `/start`
    """
    
    await message.reply("Hi \nI am Tele Bot\n created by manasa")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)


