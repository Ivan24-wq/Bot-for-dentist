from aiogram import types

#Старт
start_button = types.ReplyKeyboardMarkup(
    keyboard = [
        [types.KeyboardButton(text = "Что вас интересует?")]
    ],
    resize_keyboard=True
)

doctor_button = types.ReplyKeyboardMarkup(
    keyboard= [
        [types.KeyboardButton(text = "Записаться на приём")],
        [types.KeyboardButton(text = "Уточнить свою запись")]
    ],
    resize_keyboard=True
)