from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#Старт
start_button = types.ReplyKeyboardMarkup(
    keyboard = [
        [types.KeyboardButton(text = "Что вас интересует?")]
    ],
    resize_keyboard=True
)

doctor_button = types.ReplyKeyboardMarkup(
    keyboard= [
        [types.KeyboardButton(text = "📝Записаться на приём")],
        [types.KeyboardButton(text = "🔴Уточнить свою запись")]
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

#Функции клавуатуры месяцев для записи
def moth_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    #Прописываем месяцы
    months = [
        "Январь", "Февраль", "Март", "Апрель",
        "Май", "Июнь", "Июль", "Август", "Сентябрь",
        "Октябрь", "Ноябрь", "Декабрь"
    ]
    #По 3 кнопки в один ряд
    for i, moth in enumerate(months, start=1):
        builder.button(text=moth, callback_data=f"month_{i}")
        if i % 3 == 0:
            builder.adjust(3)
    return builder.as_markup()