import psycopg2
import os

conn = psycopg2.connect(
    host = os.environ['POSTGRES_HOST'],
    database = os.environ['POSTGRES_DB'],
    user = os.environ['POSTGRES_USER'],
    password = os.environ['POSTGRES_PASSWORD']
)

def init_db():
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transcripts (
                id SERIAL PRIMARY KEY,
                text TEXT
                )
    ''')
    conn.commit()
    cur.close()

def save_text(text):
    cur = conn.cursor()
    cur.execute('INSERT INTO transcripts (text) VALUES (%s)', (text,))
    conn.commit()
    cur.close()

def get_history():
    cur = conn.cursor()
    cur.execute('SELECT text FROM transcripts ORDER BY id DESC')
    rows = cur.fetchall()
    cur.close()
    return [r[0] for r in rows]