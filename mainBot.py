from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from aiogram.utils import executor
from text_messages import *

import random
import sqlite3
import os
from time import sleep

from forms import *
from config import *




@dp.message_handler(commands=['start'], state=None)
async def hey_user_work(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        button1, button2, button3,
        button4, button5, button6,
    )
    chat_id=types.Chat.get_current().id
    photo=open('123asd.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo, caption = start_message_text, parse_mode = 'HTML', reply_markup=keyboard)
    #await message.answer(" Выберите вариант работы", )
    
    await Form.works.set()

@dp.message_handler(commands=['Начать'], state=None)
async def hey_user_work(message: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(
        button1, button2, button3,
        button4, button5, button6,
    )
    chat_id=types.Chat.get_current().id
    photo=open('123asd.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo, caption = start_message_text, parse_mode = 'HTML', reply_markup=keyboard)
    #await message.answer(" Выберите вариант работы", )
    
    await Form.works.set()

@dp.message_handler(state=Form.works)
async def add_works(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(works=answer)
    data = await state.get_data()
    works = data.get("works")
    if works == 'Реферат':
        await message.answer(text_referat)
    elif works == 'Курсовая работа':
        await message.answer(text_cursovaya_rabota)
    elif works == 'Дипломная работа':
        await message.answer(text_diplomnaya_rabota)
    elif works == 'Научная работа':
        await message.answer(text_nauchnaya_statya)
    elif works == 'Лабораторная работа':
        await message.answer(text_laboratornaya_rabota)
    else:
        pass
    await message.answer("2️⃣ Четко и правильно сформулируйте тему Вашей работы")
    await Form.themes.set()


@dp.message_handler(state=Form.themes)
async def add_days(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(themes=answer)
    keyboard_days = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_days.add(
        button_days1, button_days2, batton_days3,
    ) 
    await message.answer("3️⃣ В какой срок необходимо выполнить работу?", reply_markup=keyboard_days)
    await Form.days.set()


@dp.message_handler(state=Form.days)
async def add_origins(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(days=answer)
    keyboard_origins = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_origins.add(
        button_origns1, button_origns2, button_origns3,
        button_origns4
    ) 
    await message.answer("4️⃣ Выберите процент оригинальности работы, если она нужна", reply_markup=keyboard_origins)
    await Form.origins.set()

@dp.message_handler(state=Form.origins)
async def add_themes(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(origins=answer)
    
    await message.answer('5️⃣ Укажите дополнительные требования ( возможно какие-то пожелания к оформлению)', reply_markup=types.ReplyKeyboardRemove())
    await Form.plus_func.set()

@dp.message_handler(state=Form.plus_func)
async def add_themes(message: types.Message, state: FSMContext):
    chat_id=types.Chat.get_current().id
    answer = message.text
    await state.update_data(plus_func=answer)
    data = await state.get_data()
    id_f = random.randint(1,9999)
    works = data.get("works")
    themes = data.get("themes")
    days = data.get("days")
    origins = data.get("origins")
    plus_func = data.get("plus_func")
    url_name = ''
    await state.finish()
    full_post_info = [(id_f, chat_id, works, themes, days, origins, plus_func,url_name)]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect(db_path)   
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tgBots_tableworks
                                (id varchar, id_user varchar, works varchar, themes varchar, days varchar,
                                origins varchar, plus_func varchar, url_name varchar)
                            """)
    cursor.executemany("INSERT INTO tgBots_tableworks VALUES (?,?,?,?,?,?,?,?)", full_post_info)
    conn.commit()
    message_text_one = f'✅Ваша заявка принята \
                \n✅Ваш уникальный ID заказа: {id_f} \
                \nДля дальнейшей работы свяжитесь с нашим специалистом, которого мы уже подобрали для вас 👇🏻 \
                \n@mad_bull69'
        
    message_text_two = f'1️⃣ Вид работы: {works}\
                \n2️⃣ Тема работы: {themes}\
                \n3️⃣ Срок выполнения: {days}\
                \n4️⃣ Оригинальность: {origins}\
                \n5️⃣ Дополнительная информация: {plus_func}'

    await bot.send_message(chat_id=chat_id, text = message_text_two)
    await bot.send_message(chat_id=chat_id, text = message_text_fake_one)
    sleep(random.randint(1,14))
    await bot.send_message(chat_id=chat_id, text = message_text_fake_two)
    sleep(random.randint(1,14))
    await bot.send_message(chat_id=chat_id, text = message_text_fake_three)
    sleep(random.randint(1,14))
    await bot.send_message(chat_id=chat_id, text = message_text_one)
    keyboard_newStart = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard_newStart.add(
        button_newStart
    ) 
    await bot.send_message(chat_id=chat_id, text = 'Для заказа новой работы нажмите на кнопку ниже', reply_markup=keyboard_newStart)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)