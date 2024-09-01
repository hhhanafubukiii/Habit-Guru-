from sqlite3 import *
from logging.config import dictConfig
from logging import *

from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

logger = getLogger(__name__)
logger.propagate = False


# РАЗБИТЬ КАЖДЫЙ СЕЛЕКТ НА МЕТОДЫ ПО ОДНОМУ

def select_user_state_db(user_id: int) -> None:
    conn = connect('../user_state.db')
    cur = conn.cursor()
    cur.execute('PRAGMA case_sensitive_like=OFF')
    cur.execute('''SELECT * FROM user_state WHERE user_id == ?''', (user_id,))

    result = cur.fetchone()
    print(result)

    conn.close()


def select_my_tea_db(user_id: int):
    conn = connect('../my_tea.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM my_tea ''',
                )
    result = cur.fetchall()

    print(result)

    conn.commit()
    logger.info(f'Был select с бд my_tea')
    conn.close()


def select_tea_parties_db(user_id: int, date: str):
    conn = connect('tea_parties.db')
    cur = conn.cursor()
    cur.execute('''SELECT 
                            tea_parties.date,
                            my_tea.tea_type, 
                            my_tea.tea_name, 
                            tea_parties.grams, 
                            tea_parties.water_temp 
                         FROM 
                            my_tea, 
                            user_state
                         WHERE 
                            tea_parties.user_id == ? AND
                            tea_parties.user_id == my_tea.user_id AND 
                            tea_parties.tea_id == my_tea.tea_id AND
                            tea.parties.date == ?''',
                (user_id, date))

    result = cur.fetchone()

    conn.commit()
    logger.info(f'Был select с бд tea_parties')
    conn.close()


select_my_tea_db(user_id=1209547541)
