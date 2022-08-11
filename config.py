from aiogram.types import KeyboardButton
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from text_messages import *
from aiogram.types import KeyboardButton

# бот
access_token = ''
bot = Bot(token=access_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# кнопки:
# Вариант работы 
button1 = KeyboardButton('Реферат')
button2 = KeyboardButton('Курсовая работа')
button3 = KeyboardButton('Дипломная работа')
button4 = KeyboardButton('Научная работа')
button5 = KeyboardButton('Лабораторная работа')
button6 = KeyboardButton('Другой вариант')

# срок выполнения работы 
button_days1 = KeyboardButton('От 1 до 5 дней')
button_days2 = KeyboardButton('От 5 до 10 дней')
batton_days3 = KeyboardButton('От 10 и более дней')

# Оригинальность работы 
button_origns1 = KeyboardButton(f'50% - 70%')
button_origns2 = KeyboardButton(f'71% - 90%')
button_origns3 = KeyboardButton(f'90% - 100%')
button_origns4 = KeyboardButton(f'Без оригинальности')

# Новый старт
button_newStart = KeyboardButton(f'/Начать')