from aiogram import *
import random
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot('6274614032:AAEMhf8KaZECN34avWgzM-dUQQFoy7dSZGs')
dp = Dispatcher(bot=bot)

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Овен').add('Телец').add('Близнецы').add('Рак').add('Лев').add('Дева').add('Весы')\
    .add('Скорпион').add('Стрелец').add('Козерог').add('Водолей').add('Рыбы')


first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('hi choose your znak zodiak', reply_markup=main_admin)


@dp.message_handler(text='Овен')
async def oven(message: types.Message):
    await message.answer(random.choice(first))


@dp.message_handler(text='Весы')
async def oven(message: types.Message):
    await message.answer(random.choice(second))

@dp.message_handler(text='Лев')
async def oven(message: types.Message):
    await message.answer(random.choice(first))

@dp.message_handler(text='Скорпион')
async def oven(message: types.Message):
    await message.answer(random.choice(first))

@dp.message_handler(text='Стрелец')
async def oven(message: types.Message):
    await message.answer(random.choice(third))
@dp.message_handler(text='Козерог')
async def oven(message: types.Message):
    await message.answer(random.choice(second))
@dp.message_handler(text='Водолей')
async def oven(message: types.Message):
    await message.answer(random.choice(first))
@dp.message_handler(text='Рыбы')
async def oven(message: types.Message):
    await message.answer(random.choice(first))
@dp.message_handler(text='Близнецы')
async def oven(message: types.Message):
    await message.answer(random.choice(second_add))
@dp.message_handler(text='Телец')
async def oven(message: types.Message):
    await message.answer(random.choice(first))
@dp.message_handler(text='Рак')
async def oven(message: types.Message):
    await message.answer(random.choice(third))
@dp.message_handler(text='Дева')
async def oven(message: types.Message):
    await message.answer(random.choice(second))









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)