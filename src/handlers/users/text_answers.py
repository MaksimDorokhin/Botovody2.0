from asyncio import sleep
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from loader import dp, db
from geopy.geocoders import Nominatim


@dp.message_handler(text="О нас")
async def answer_about_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text="Здесь отображается какая-то информация о магазине",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="Контакты")
async def answer_contacts_command(message: types.Message):
    await types.ChatActions.upload_document()
    await sleep(0.2)
    await message.answer_contact("+79160890777", "Максим", "Дорохин",
                                 reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="График работы")
async def answer_working_time_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text="Ежедневно с 9:00 до 20:00 без выходных!",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text="О боте")
async def answer_about_bot_command(message: types.Message):
    await types.ChatActions.choose_sticker()
    await sleep(0.2)
    await message.answer_sticker('CAACAgIAAxkBAAEF0h5jH4rgJj9JivNBSx0mwtlJjlHJPwACggAD3rG5GJ0yXxG8M1cHKQQ',
                                 reply_markup=ReplyKeyboardRemove())



@dp.message_handler(commands="add")
async def answer_start_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text="Вы пытаетесь что-то добавить\n",
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(startswith=["Покажи", "Показать", "покажи", "показать"]))
async def answer_show_command(message: types.Message):
    if len(message.text.split(" ", maxsplit=1)) > 1:
        await types.ChatActions.typing()
        await sleep(0.2)
        await message.reply("Лови:")
        await types.ChatActions.upload_photo()
        await sleep(0.2)
        await message.answer_photo(f'https://yandex.ru/images/search?text={message.text.split(" ", maxsplit=1)[1]}')
    else:
        await types.ChatActions.typing()
        await sleep(0.2)
        await message.reply("Напиши хоть что-нибудь в запросе!")


@dp.message_handler(content_types=['contact'])
async def answer_send_contact_command(message: types.Message):
    if message.from_user.id == message.contact.user_id:
        await types.ChatActions.typing()
        await sleep(0.2)
        await message.answer(text='Регистрация прошла успешно!',
                             reply_markup=ReplyKeyboardRemove())
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await types.ChatActions.typing()
        await sleep(0.2)
        await message.answer(text='А это кто?',
                             reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types=['location'])
async def answer_location_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text=f'Широта: {message.location.latitude}\n'
                         f'долгота: {message.location.longitude}',
                         reply_markup=ReplyKeyboardRemove())
    geolocator = Nominatim(user_agent="<<some_app_name>>")
    location = geolocator.reverse(f"{message.location.latitude}, {message.location.longitude}")
    await message.answer(f'{location.address}')


@dp.message_handler()
async def answer_not_known_command(message: types.Message):
    await types.ChatActions.typing()
    await sleep(0.2)
    await message.answer(text='Мая твая не панимая!',
                         reply_markup=ReplyKeyboardRemove())
