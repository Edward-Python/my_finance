from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message, ReplyKeyboardRemove

from handlers import keyboard


category_router = Router()


class Category(StatesGroup):
    category = State()


@category_router.message(StateFilter(None),\
                         F.text=="📝Создание названий статей расход")
async def category_add(message: Message, state: FSMContext):
    await message.answer(text="введите название статьи расхода",\
                        reply_markup=ReplyKeyboardRemove())
    await state.set_state(Category.category)


@category_router.message(Category.category, F.text)
async def category_name_input(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer(text="Название статьи сохранено")
    await message.answer(text="выберите действие",\
                         reply_markup=keyboard.menu_keyboard())    
    input_category = await state.get_data()
    list_category = list(input_category.values())
    category = list_category[0]
    print(category) # DB
    await state.clear()