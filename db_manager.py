#! /usr/bin/env python3

import sqlite3

# titre
# description
# duree
# nombre de vue
# url de la thumbnail de la video

def make_query(query):
    pass

def create_db():
    query = '''CREATE TABLE videos_data\
               (id text primary key, title text, description text,\
               duration real, views real, thumbnail_url text)'''

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute(query)

    conn.commit()

    conn.close()

def insert_data(video_data):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('INSERT INTO videos_data VALUES (?,?,?,?,?,?)', video_data)

    conn.commit()

    conn.close()

def is_video_present(idVideo):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    
    tupleData = (idVideo,)

    c.execute('SELECT * FROM videos_data WHERE id=?', tupleData)

    result = True if c.fetchone() is not None else False

    c.close()

    return result
