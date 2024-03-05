from aiogram.dispatcher.filters.state import State, StatesGroup


class Bolimlar(StatesGroup):
    setlar = State()
    lavash = State()
    shaurma = State()
    burger = State()
    hotdog = State()
    ichimliklar = State()
    shirinliklar = State()
    garnirlar = State()

    barcha_menyular = State()
