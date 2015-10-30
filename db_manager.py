#! /usr/bin/env python3

import sqlite3

# id
# title
# description
# duration
# views
# thumbnail url

def print_data(row_data):
    """
        Print the informations of the video stored in `row_data`.
    """
    m, s = divmod(row_data[3], 60)
    h, m = divmod(m, 60)
    duration = "%02d:%02d:%02d" % (h, m, s)
    print("Informations of the video:\n"
          " * id: %s\n"
          " * title: %s\n"
          " * description: %s"
          % row_data[:3])
    print(" * duration: %s" % duration)
    print(" * views: %d\n"
          " * thumbnail url: %s"
          % row_data[4:])

def create_db():
    """
        Create the database with the videos_data table.
    """
    query = '''CREATE TABLE videos_data\
               (id text primary key, title text, description text,\
               duration integer, views integer, thumbnail_url text)'''

    conn = sqlite3.connect('videos_data.db')
    c = conn.cursor()
    c.execute(query)

    conn.commit()

    conn.close()

def insert_data(video_data):
    """
        Insert `video_data` row in the database.
    """
    conn = sqlite3.connect('videos_data.db')
    c = conn.cursor()
    c.execute('INSERT INTO videos_data VALUES (?,?,?,?,?,?)', video_data)

    conn.commit()

    conn.close()

def get_video_infos(idVideo):
    """
        Retrieve the information of the video corresponding to `idVideo`.
    """
    conn = sqlite3.connect('videos_data.db')
    c = conn.cursor()
    
    tupleData = (idVideo,)

    c.execute('SELECT * FROM videos_data WHERE id=?', tupleData)

    result = c.fetchone()

    c.close()

    return result
