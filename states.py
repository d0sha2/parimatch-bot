from aiogram.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    Base = State()
    CREATING_PARI = State()
    