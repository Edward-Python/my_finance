from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="📝Ввод данных доход/расход"),
        KeyboardButton(text="📝Создание названий статей доход/расход"),
        KeyboardButton(text="📝Баланс")
    ), builder.adjust(1,1,1)
    return builder.as_markup(resize_keyboard=True)


def consum_income():
    builder1 = ReplyKeyboardBuilder()
    builder1.add(
        KeyboardButton(text="📝Введите доход"),
        KeyboardButton(text="📝Введите расход"),
        KeyboardButton(text="👈Вернуться назад")
    ), builder1.adjust(2,1)
    return builder1.as_markup(resize_keyboard=True)


def income():
    builder3 = ReplyKeyboardBuilder()
    builder3.add(
        KeyboardButton(text="✔Готово"),
        KeyboardButton(text="👈Вернуться назад")
    ), builder3.adjust(1,1)
    return builder3.as_markup(resize_keyboard=True)


def consumption():
    builder2 = ReplyKeyboardBuilder()
    builder2.add(
        KeyboardButton(text="✔Готово"),
        KeyboardButton(text="👈Вернуться назад")
    ), builder2.adjust(1,1)
    return builder2.as_markup(resize_keyboard=True)


