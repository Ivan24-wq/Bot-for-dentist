from aiogram import types

#Старт
start_button = types.ReplyKeyboardMarkup(
    keyboard = [
        [types.KeyboardButton(text = "Что вас интересует?")]
    ],
    resize_keyboard=True
)