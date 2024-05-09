from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from handlers import keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text="👇Выберите действие👇",
                         reply_markup=keyboard.menu_keyboard()) # добавить доход, расход, баланс


@router.message(F.text == "📝Ввод данных доход/расход")
async def write_data(message: Message):
    # while != готово(кнопка)
    await message.answer(text="👇Выберите действие👇",\
                         reply_markup=keyboard.consum_income())
    # доход(кнопка) и расход (кнопка)
    # готово (кнопка)
    # break

@router.message(F.text == "📝Введите доход")
async def income(message: Message):
    await message.answer(text="👇Введите сумму дохода",\
                         reply_markup=keyboard.income())
    await message.answer(text="OK",\
                         reply_markup=keyboard.income())
    

@router.message(F.text == "📝Введите расход")
async def income(message: Message):
    await message.answer(text="👇Введите сумму расхода",\
                         reply_markup=keyboard.consumption())

    # await message.answer(text="Давай создадим названия статей расходов/доходов.\
    #                      Для подтверждения нажми кнопку доход или расход.")