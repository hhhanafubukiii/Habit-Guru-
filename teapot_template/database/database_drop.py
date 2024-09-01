from sqlite3 import *
from logging import *
from logging.config import dictConfig

from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

conn = None
logger = getLogger(__name__)
logger.propagate = False


def delete_user_state_db():
    global conn
    conn = connect('../user_state.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS user_state')

    conn.commit()
    logger.info('База данных user_state была удалена')
    conn.close()


def delete_tea_parties_db():
    global conn
    conn = connect('../tea_parties.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS tea_parties')

    conn.commit()
    logger.info('База данных tea_parties была удалена')
    conn.close()


def delete_my_tea_db():
    global conn
    conn = connect('../my_tea.db')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS my_tea')

    conn.commit()
    logger.info('База данных my_tea была удалена')
    conn.close()


delete_my_tea_db()
