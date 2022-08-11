from django.http import *
from django.shortcuts import redirect, render
from tgBots.forms import *
from tgBots.models import TableWorks
from django.views.generic.list import ListView
import os
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


TOKEN_client ='5184134875:AAEytNLoJf_PK0FblHHpKVl1d3k6c7SO1vs'

TOKEN_admin = '5472667053:AAE9QsmxhwQscvSoZFt4y19ikbmMen4Omvs'

bot_admin = Bot(token=TOKEN_admin)

dp_admin = Dispatcher(bot_admin, storage=MemoryStorage())

bot_client = Bot(token=TOKEN_client)

dp_client = Dispatcher(bot_admin, storage=MemoryStorage())


class DataProject:
    def __init__(self) -> None:
         pass

    table = TableWorks.objects.all()
    for el in table:
                works = el.works
                themes = el.themes
                days = el.days
                origins =  el.origins
                plus_func = el.plus_func
                sid = el.id
                id_user =el.id_user
    

    
        

def index(request):
        table1 = TableWorks.objects.all()
        form = IdUser()
        if request.method == "POST":
                    form = IdUser(request.POST)
                    if form.is_valid():
                        x = form.cleaned_data
                        url_name = (x['url_name'])
                        id_work = (x['id_works'])
                        print(url_name, id_work)
                        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

                        db_path = os.path.join(BASE_DIR, "db.sqlite3")

                        conn = sqlite3.connect("db.sqlite3")

                        cursor = conn.cursor()

                        sql_update_query = """UPDATE tgBots_tableworks SET url_name = ? WHERE id = ?"""

                        cursor.execute(sql_update_query, (url_name, id_work ))

                        records = cursor.fetchall()

                        conn.commit()
                        
                    else:
                        form = IdUser()
        return render(request, 'index.html',{'table': table1, 'form': form}, )

def deleteInt(request, user_id, work_id):
    table = TableWorks.objects.get(pk=work_id)

    async def send_message(id_user, table):
        
        await bot_client.send_message(chat_id=id_user, text=f' Ваш заказ ID: {work_id} \
           \n Тема заказа {table.themes}  выполнен \
           \n Ссылка для скачивания {table.url_name}')
           
    asyncio.run(send_message(user_id, table))
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql_update_query = """DELETE from tgBots_tableworks where id = ?"""
    cursor.execute(sql_update_query, (work_id, ))
    records = cursor.fetchall()
    conn.commit()
    return redirect('index')



