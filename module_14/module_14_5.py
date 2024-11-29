"""
Домашнее задание по теме "Написание примитивной ORM"
Цель: написать простейшие CRUD функции для взаимодействия с базой данных.
Задача "Регистрация покупателей":
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions as cfs

products = cfs.get_all_products()  # подгружаем из БД Продукты из предыдущего задания

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()  # возраст, полных лет
    growth = State()  # рост, см
    weight = State()  # вес, кг


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)  # , one_time_keyboard=True
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button1, button2)
kb.add(button3, button4)

kib = InlineKeyboardMarkup(resize_keyboard=True)

inline_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kib.add(inline_button1, inline_button2)

kib_buy = InlineKeyboardMarkup()
inline_button1_buy = InlineKeyboardButton(text='Продукт 1', callback_data="product_buying")
inline_button2_buy = InlineKeyboardButton(text='Продукт 2', callback_data="product_buying")
inline_button3_buy = InlineKeyboardButton(text='Продукт 3', callback_data="product_buying")
inline_button4_buy = InlineKeyboardButton(text='Продукт 4', callback_data="product_buying")
kib_buy.row(inline_button1_buy, inline_button2_buy, inline_button3_buy, inline_button4_buy)

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
buttom_start = KeyboardButton(text='/start')
kb_start.add(buttom_start)


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст (полных лет):')
    await call.answer()
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
    weight = data.get('weight')
    growth = data.get('growth')
    age = data.get('age')
    # c, b, a = data.values()
    # calc = (10 * weight) + (6.25 * growth) - (5 * age) + 5
    # calc = (10 * a) + (6.25 * b) - (5 * c) - 161
    calc = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f"Ваша норма калорий:{calc}")
    await state.finish()


# Для мужчин: ПБМ = (10 × вес в кг) + (6, 25 × рост в см) − (5 × возраст в годах) + 5.
# Для женщин: ПБМ = (10 × вес в кг) + (6, 25 × рост в см) − (5 × возраст в годах) − 161.


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def start(message):
    await message.answer("Я бот помогающий твоему здоровью, расчитываю норму калорий на сутки по формуле Формула "
                         "Миффлина-Сан Жеора ", reply_markup=kb)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('ПБМ = (10 × вес в кг) + (6, 25 × рост в см) − (5 × возраст в годах) − 161')
    await call.answer()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kib)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for product in products:
        with open(f'picture/product{product[0]}.png', "rb") as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kib_buy)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text=['Регистрация'])
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if cfs.is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя:')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data_user = await state.get_data()
    username = data_user.get('username')
    email = data_user.get('email')
    age = data_user.get('age')
    cfs.add_user(username, email, age)
    await message.answer(f"Пользователь {username} зарегистрирован")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer('Для работы Бота педалируй /start:', reply_markup=kb_start)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
