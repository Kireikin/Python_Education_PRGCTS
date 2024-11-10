from aiogram import Bot, Dispatcher, executor  # , types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start():
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start(dp, 12, skip_updates=True)
