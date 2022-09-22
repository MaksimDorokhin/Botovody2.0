from asyncio import sleep
from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards import commands_default_keyboard, commands_info_keyboard


@dp.message_handler(text=["Помощь", "помощь", "Меню"])
@dp.message_handler(commands="help")
async def answer_help_command(message: types.Message):
    await message.answer(text='Список команд представлен на клавиатуре',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(text=["Информация", "информация", "Инфо", "инфо"])
@dp.message_handler(commands="info")
async def answer_start_command(message: types.Message):
    await message.answer(text='Список команд представлен на клавиатуре',
                         reply_markup=commands_info_keyboard)


@dp.message_handler(text=["Привет", "привет", "Начать", "начать"])
@dp.message_handler(commands="start")
async def answer_start_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text=f"Привет {message.from_user.first_name}\n"
                              "Рад тебя видеть!",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands="item")
async def answer_item_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text='У нас в наличии:'
                              '\n - редис'
                              '\n - помидоры'
                              '\n - капуста',
                         reply_markup=ReplyKeyboardRemove())