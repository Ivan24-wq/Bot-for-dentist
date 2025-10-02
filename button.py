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

#Уточнения свободных мест
freeplaces_button = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text = "Посмотреть свободные места для записи")]
    ],
    resize_keyboard=True
)


#Отмена записи
cancel_button = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text = "Отменить запись", callback_data="cancel")]
    ]
)