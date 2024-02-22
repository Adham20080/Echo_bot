import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import Token

bot = Bot(token=Token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "<b>Assalomu alaykum!</b> Xush kelibsiz.\n\n<i>Echo botga xush kelibsiz</i>",
        parse_mode="HTML")


@dp.message()
async def echo(message: types.Message):
    await message.reply(f"<b>{message.text}</b>", parse_mode="HTML")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
