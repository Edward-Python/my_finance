from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="📝Ввод данных расход"),
        KeyboardButton(text="📝Создание названий статей расход"),
        KeyboardButton(text="📝Баланс")
    ), builder.adjust(1,1,1)
    return builder.as_markup(resize_keyboard=True)


# def consum_income():
#     builder1 = ReplyKeyboardBuilder()
#     builder1.add(
#         KeyboardButton(text="📝доход"),
#         KeyboardButton(text="📝расход"),
#         KeyboardButton(text="👈Вернуться назад")
#     ), builder1.adjust(2,1)
#     return builder1.as_markup(resize_keyboard=True)


# def income():
#     builder2 = ReplyKeyboardBuilder()
#     builder2.add(
#         KeyboardButton(text="✔Готово"),
#         KeyboardButton(text="👈Вернуться назад")
#     ), builder2.adjust(1,1)
#     return builder2.as_markup(resize_keyboard=True)


def consumption():
    builder3 = ReplyKeyboardBuilder()
    builder3.add(
        KeyboardButton(text="✔Готово")
    )
    return builder3.as_markup(resize_keyboard=True)


# def alphabet():
#     alphabet = []
#     for i in range(ord("а"), ord("я")):
#         alphabet.append(chr(i))
#     print(alphabet)
#     buiider_alhpabet = ReplyKeyboardBuilder()
#     buiider_alhpabet.add(
#         KeyboardButton(text=alphabet),
#         KeyboardButton(text="✔Готово"),
#         KeyboardButton(text="👈Вернуться назад")
#     ), buiider_alhpabet.adjust(1,1)
#     return buiider_alhpabet.as_markup(resize_keyboard=True)