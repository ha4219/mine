import sqlite3


def insert_data(date, score):
    try:
        conn = sqlite3.connect("score.db")
        cur = conn.cursor()

        sql = "insert into score(date, score) values (?, ?)"
        cur.execute(sql, (date, score))
        conn.commit()

        conn.close()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
