import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import KeyboardBuilder
from button import start_button, doctor_button, cancel_button
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
    await message.answer("Выберите услугу", reply_markup=doctor_button)
    
#Обработка записи на приём
@dp.message(F.text == "Записаться на приём")
async def process_list(message: types.Message):
    await message.answer("Хорошо, давайте выберем дату")

#Уточняеем запись
@dp.message(F.text == "Уточнить свою запись")
async def progress_check(message: types.Message):
    await message.answer("Введите ваши данные для уточнения записи!", reply_markup=cancel_button)
    
#Обработчик записи
@dp.message(F.text == "Посмотреть свободные места для записи")
async def check_places(message: types.Message):
    await message.answer("Свободные места есть: ")
    
#Отмена    
@dp.callback_query(lambda c: c.data == "cancel")
async def cancel_place(callback_querty: types.CallbackQuery):
    await callback_querty.answer("Вы отменили свою запись")
    await callback_querty.answer()

#Запуск процесса полинга
async def main():
    await dp.start_polling(bot)

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())