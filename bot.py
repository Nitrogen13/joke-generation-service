import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from constants import API_TOKEN
from gpt2_model import MODEL, TOKENIZER, ARGS

sys.path.append("./ruGPT2")
from ruGPT2.generate_samples import (
    generate_samples_unconditional,
    generate_samples_input_from_file,
    generate_samples_interactive,
)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(regexp="Generate joke")
async def generate_joke(message: types.Message):
    await types.ChatActions.typing()
    print("Generating joke ...")
    await message.reply(
        next(generate_samples_unconditional(MODEL, TOKENIZER, ARGS))["text"],
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
    await types.ChatActions.typing()
    print("Generating joke from context ...")

    ARGS.text = message.text
    await message.reply(
        next(generate_samples_interactive(MODEL, TOKENIZER, ARGS)),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Generate joke")]], resize_keyboard=True
        ),
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
