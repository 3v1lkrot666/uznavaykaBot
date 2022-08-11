from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    works = State() 
    themes = State() 
    days = State()
    origins = State() 
    plus_func = State() 
