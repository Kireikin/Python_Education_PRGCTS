from pprint import pprint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()  # возраст, полных лет
    growth = State()  # рост, см
    weight = State()  # вес, кг


@dp.message_handler(text=['Calories', 'c'])
async def set_age(message):
    await message.answer('Введите свой возраст (полных лет):')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост (см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес (кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    pprint(data)
    print(data.get('weight'))
    weight = data.get('weight')
    growth = data.get('growth')
    age = data.get('age')
    # c, b, a = data.values()
    calc = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    # calc = (10 * data['weight']) + (6.25 * data['growth']) - (5 * data['age']) - 161
    # calc = (10 * a) + (6.25 * b) - (5 * c) - 161
    await message.answer(f"Ваша норма калорий:{calc}")
    await state.finish()
# Для мужчин: ПБМ = (10 × вес в кг) + (6, 25 × рост в см) − (5 × возраст в годах) + 5.
# Для женщин: ПБМ = (10 × вес в кг) + (6, 25 × рост в см) − (5 × возраст в годах) − 161.


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью, введите 'Calories' или 'c' для ввода данных и "
                         "расчёта")


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
