from sqlite3 import *
from logging.config import dictConfig
from logging import *
from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

conn = None
logger = getLogger(__name__)
logger.propagate = False


def delete_from_user_state_db(user_id: int) -> None:
    global conn
    conn = connect('../user_state.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM user_state 
                   WHERE user_id == ?''',
                (user_id,))

    conn.commit()
    logger.info(f'Пользователь {user_id} был удален из user_state')
    conn.close()


def delete_from_my_tea_db(user_id: int) -> None:  # tea_name: str, prod_year: int
    global conn
    conn = connect('../my_tea.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM my_tea
                   WHERE user_id == ?''',
                (user_id, ))

    conn.commit()
    logger.info(f'Пользователь {user_id} был удален из user_state')
    conn.close()


def delete_from_tea_parties_db(user_id: int, date: str):
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()

    cur.execute('''DELETE FROM user_state 
                   WHERE user_id == ?''',
                (user_id,))

    conn.commit()
    logger.info(f'Пользователь {user_id} был удален из user_state')
    conn.close()


# delete_from_my_tea_db(user_id=7288418154)


