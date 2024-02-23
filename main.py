import asyncio
import logging
import random
from aiogram import Bot, Router, Dispatcher, types, F
from aiogram.filters.command import Command
from config import Token

dp = Dispatcher()
rt = Router()
bot = Bot(token=Token)
logging.basicConfig(level=logging.INFO)
key = [
    [types.KeyboardButton(text="/random")],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "<b>Assalomu alaykum!</b> Xush kelibsiz.\n\n<i>Echo botga xush kelibsiz</i>",
        parse_mode="HTML", reply_markup=keyboard)


@dp.message(Command("random"))
async def start(message: types.Message):
    a = random.randint(1, 11)
    print(a)
    await message.answer(
        "<b>Men bir son o'ylayman, siz esa topasiz.</b>\n\n<i>Bu son 1 dan 10 gacha.</i>", parse_mode="HTML")


@dp.message(F.text.isdigit())
async def echo(message: types.Message):
    a = random.randint(1, 11)
    b = message.text
    if a == int(b):
        print(a)
        await message.reply(f"<b>To'gri topdingiz.</b>", parse_mode="HTML")
    else:
        await message.answer_photo("https://wallpapercave.com/wp/wp6725007.png", caption="O'yin tugadi 😑")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
