import sqlite3, random, datetime
from model import Playlist


Playlists = [
    {
        'name':'Darker Faces',
        'songs':'4'
    },
        {
        'name':'Face My fears',
        'songs':'5'
    },
]    

def getNewId():
    return random.getrandbits(28)

def connect():
    conn = sqlite3.connect('Playlists.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Playlists (id INTEGER PRIMARY KEY, name TEXT,songs INTEGER)")
    conn.commit()
    conn.close()
    for i in Playlists:
        pl = Playlist(getNewId(), i['name'], i['songs'])
        insert(pl)

def insert(pl):
    conn = sqlite3.connect('Playlists.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Playlists VALUES (?,?,?)", (
        pl.id,
        pl.name,
        pl.songs,
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('Playlists.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Playlists")
    rows = cur.fetchall()
    viewer = []
    for i in rows:
        pl = Playlist(i[0], i[1], i[2])
        viewer.append(pl)
    conn.close()
    return viewer

def delete(theId):
    conn = sqlite3.connect('Playlists.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Playlists WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('Playlists.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Songs")
    conn.commit()
    conn.close()