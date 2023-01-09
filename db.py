import sqlite3, random, datetime
from model import Song


Songs = [
    {
        'title': 'Pefect',
        'album':'21',
        'artist':'Ed Sheeran',
    }
]    

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect('Songs.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Songs (id INTEGER PRIMARY KEY, title TEXT,album TEXT, artist TEXT)")
    
    conn.commit()
    conn.close()
    for i in Songs:
        sg = Song(getNewId(), i['title'], i['album'], i['artist'])
        insert(sg)

def insert(sg):
    conn = sqlite3.connect('Songs.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Songs VALUES (?,?,?,?)", (
        sg.id,
        sg.title,
        sg.album,
        sg.artist
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('Songs.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Songs")
    rows = cur.fetchall()
    viewer = []
    for i in rows:
        sg = Song(i[0], i[1], i[2], i[3])
        viewer.append(sg)
    conn.close()
    return viewer

def delete(theId):
    conn = sqlite3.connect('Songs.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Songs WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('Songs.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Songs")
    conn.commit()
    conn.close()