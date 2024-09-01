from sqlite3 import *
from logging.config import dictConfig
from logging import *
from teapot_template.config_data.logging.logging_settings import logging_config

dictConfig(logging_config)

conn = None
logger = getLogger(__name__)
logger.propagate = False


# -----------------CREATE-------------------
def create_my_tea_db() -> None:
    global conn
    conn = connect('../my_tea.db')
    cur = conn.cursor()
    cur.execute('''PRAGMA foreign_keys=ON''')
    cur.execute('''CREATE TABLE IF NOT EXISTS my_tea(
    tea_id INTEGER PRIMARY KEY NOT NULL, 
    user_id INTEGER, 
    tea_type TEXT, 
    tea_name TEXT, 
    prod_year INTEGER, 
    rate INTEGER, 
    descr TEXT,
    FOREIGN KEY(user_id) REFERENCES user_state(user_id))''')

    conn.commit()
    logger.info('Была создана база данных my_tea')
    conn.close()


def create_tea_parties_db() -> None:
    global conn
    conn = connect('../tea_parties.db')
    cur = conn.cursor()
    cur.execute('''PRAGMA foreign_keys=ON''')
    cur.execute('''CREATE TABLE IF NOT EXISTS tea_parties(
    user_id INTEGER, 
    party_id INTEGER,
    tea_id INTEGER
    grams REAL, 
    water_temp INTEGER, 
    date BLOB,
    FOREIGN KEY(user_id) REFERENCES user_state(user_id),
    FOREIGN KEY(tea_id) REFERENCES my_tea(tea_id))''')

    conn.commit()
    logger.info('Была создана база данных tea_parties')
    conn.close()


def create_user_state_db() -> None:
    global conn
    conn = connect('../user_state.db')
    cur = conn.cursor()
    cur.execute('''PRAGMA foreign_keys=ON''')
    cur.execute('''CREATE TABLE IF NOT EXISTS user_state(
                    user_id INTEGER, 
                    state TEXT, 
                    total_parties INTEGER)''')

    conn.commit()
    logger.info('Была создана база данных user_state')
    conn.close()


