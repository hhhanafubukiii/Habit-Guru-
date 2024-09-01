from sqlite3 import *
from logging import *
from logging.config import dictConfig

from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

conn = None
logger = getLogger(__name__)
logger.propagate = False


def insert_user_state_db(user_id: int,
                         state: str,
                         total_parties: int) -> None:
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO user_state(user_id, state, total_parties) 
                         VALUES (?, ?, ?)''',
                (user_id, state, total_parties))

    conn.commit()
    logger.info(f'Пользователь {user_id} добавился в базу данных user_state')
    conn.close()


def insert_tea_parties_db(user_id: int,
                          party_id: int,
                          grams: float | None,
                          water_temp: int | None,
                          date: list[str]) -> None:
    global conn
    conn = connect('database/user_state.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO tea_parties(party_id, 
                                                 grams, 
                                                 water_temp, 
                                                 date) 
                         VALUES (?, ?, ?, ?)''',
                (party_id, grams, water_temp, date))

    conn.commit()
    logger.info(f'Пользователь {user_id} добавился в базу данных user_state')
    conn.close()


def insert_my_tea_db(tea_list) -> None:
    global conn
    conn = connect('my_tea.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO my_tea(user_id, 
                                            tea_type, 
                                            tea_name, 
                                            prod_year, 
                                            rate, 
                                            descr) 
                         VALUES (?, ?, ?, ?, ?, ?)''',
                (tea_list[0], tea_list[1], tea_list[2], tea_list[3], tea_list[4], tea_list[5]))

    conn.commit()
    conn.close()


