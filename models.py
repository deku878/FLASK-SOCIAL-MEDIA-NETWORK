from os import path
import sqlite3 as sql

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO posts (name, content) VALUES (?, ?)', (name, content))  # 'name' instead of 'names'
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    con.close()
    return posts
