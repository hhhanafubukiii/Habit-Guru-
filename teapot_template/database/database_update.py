from sqlite3 import *
from logging import *
from logging.config import dictConfig

from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

conn = None
logger = getLogger(__name__)


def update_state_in_user_state_db(user_id: int, state: str):  # total_parties: int):
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()
    cur.execute('''UPDATE user_state
                   SET state = ?
                   WHERE user_id == ?''',
                (state, user_id))

    conn.commit()
    logger.info(f'Была изменена бд user_state - user_id: {user_id}')
    conn.close()


def update_total_parties_in_user_state_db(user_id: int, total_parties: int):  # total_parties: int):
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()
    cur.execute('''UPDATE user_state
                   SET total_parties = ?
                   WHERE user_id == ?''',
                (total_parties, user_id))

    conn.commit()
    logger.info(f'Была изменена бд user_state - user_id: {user_id}')
    conn.close()


# НЕ ДОДЕЛАНО!!!
def update_my_tea_db(user_id: int, tea_type: str, tea_name: str, prod_year: int,
                     new_tea_type: str, new_tea_name: str, new_prod_year: int, new_rate: int, new_descr: int):
    global conn
    conn = connect('my_tea.db')
    cur = conn.cursor()
    cur.execute('''UPDATE my_tea
                   SET tea_type = ?, tea_name = ?, prod_year = ?, rate = ?, descr = ?
                   WHERE user_id == ? AND (tea_type == ? OR tea_name == ? OR prod_year == ?)''',
                (new_tea_type, new_tea_name, new_prod_year, new_rate, new_descr,
                 user_id, tea_type, tea_name, prod_year))

    conn.commit()
    logger.info(f'Была изменена бд user_state - user_id: {user_id}')
    conn.close()


def update_tea_parties_db(user_id: int, date: str, tea_type: str, tea_name: str, prod_year,
                          new_grams: float, new_water_temp: int):
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()

    cur.execute('''SELECT
                        tea_id
                    FROM my_tea
                    WHERE user_id == ? AND (tea_type == ? OR tea_name == ? OR prod_year == ?)''',
                (user_id, tea_type, tea_name, prod_year))
    new_tea_id = cur.fetchone()[0]

    cur.execute('''UPDATE tea_parties 
                         SET tea_parties.tea_id = ?, tea_parties.grams = ?, tea_parties.water_temp = ?
                         WHERE user_id == ? AND date == ?''',
                (new_tea_id, new_grams, new_water_temp, user_id, date))

    conn.commit()
    logger.info(f'Была изменена бд tea_parties -  user_id: {user_id}')
    conn.close()
