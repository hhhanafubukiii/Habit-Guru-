from aiogram.fsm.state import default_state, State, StatesGroup


class FSMFillForm(StatesGroup):
    
    new_tea_party = State()
    fill_tea_type = State()
    fill_tea_name = State()
    fill_prod_year = State()
    fill_tea_grade = State()
    fill_tea_description = State()
    confirm_state = State()

    fill_grams_amount = State()
    fill_water_temp = State()
    