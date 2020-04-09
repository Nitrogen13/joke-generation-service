import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from constants import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(regexp="Generate joke")
async def generate_joke(message: types.Message):
    await types.ChatActions.typing()

    await message.reply(
        "Sample joke",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Generate joke")]], resize_keyboard=True
        ),
    )


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await types.ChatActions.typing()

    await message.reply(
        "Hello, I can generate jokes for you!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Generate joke")]], resize_keyboard=True
        ),
    )


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Just press "Generate joke" button!')
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
