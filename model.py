class Song():
  def __init__(self, id, title, artist,album):
    self.id=id
    self.title=title
    self.album=album
    self.artist=artist

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'album': self.album,
      'artist':self.artist,
    }   

class Playlist():
  def __init__(self, id, name, songs):
    self.id=id
    self.name=name
    self.songs=songs

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'songs': self.songs,
    }   