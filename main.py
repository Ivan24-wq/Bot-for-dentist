import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import KeyboardBuilder
from button import start_button
from dotenv import load_dotenv
import os

load_dotenv()

#Логирование
logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("Token")
bot = Bot(token = TOKEN)
dp = Dispatcher()

#start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Рад тебя видеть!", reply_markup=start_button)
    

@dp.message(F.text == "Что вас интересует?")
async def process_start(message: types.Message):
    await message.answer("Выберите услугу")
    
#Запуск процесса полинга
async def main():
    await dp.start_polling(bot)

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())