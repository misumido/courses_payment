from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    number_st = State()
    payment_st = State()