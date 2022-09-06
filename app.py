from asyncio import sleep

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from os import getenv
from sys import exit

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(text=["Помощь", "помощь"])
@dp.message_handler(commands="help")
async def answer_start_comand(message: types.Message):
    await message.answer(text="Привет! Пока я умею только здороваться (/start)\n"
                              "И показывать вам картинки по запросу (Покажи <ваш запрос>)")


@dp.message_handler(text=["Привет", "Начать"])
@dp.message_handler(commands="start")
async def answer_start_comand(message: types.Message):
    await message.answer(text="Трям, здравствуй!\n"
                              "Рад тебя видеть!")


@dp.message_handler(Text(startswith=["Покажи", "Показать", "покажи", "показать"]))
async def answer_show_comand(message: types.Message):
    await types.ChatActions.typing()
    await sleep(1)
    await message.reply("Лови:")
    await types.ChatActions.upload_photo()
    await sleep(1)
    await message.answer_photo(f'https://yandex.ru/images/search?text={message.text.split(" ")[1]}')

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
