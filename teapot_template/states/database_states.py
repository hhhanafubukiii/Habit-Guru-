from sqlite3 import *

conn = None


def is_in_db(user_id: int) -> bool:
    global conn
    conn = connect('user_state.db')
    cur = conn.cursor()
    cur.execute('''SELECT user_id, state, total_parties
                   FROM user_state
                   WHERE user_id == ?''',
                (user_id, ))
    result = cur.fetchone()
    print(f'result1 is {result}')
    if result is None:
        return True
    else:
        return False
