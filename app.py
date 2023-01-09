from flask import Flask, render_template, request, jsonify
import os, re, datetime
import db,db1
from model import Song,Playlist

app = Flask(__name__)

if not os.path.isfile('Songs.db'):
    db.connect()

if not os.path.isfile('Playlist.db'):
    db1.connect()

@app.route("/")
def index():
    # db.connect()
    # db1.connect()
    return "Database Connected"

@app.route('/playlists', methods=['GET'])
def getplayRequest():
    # db.connect()
    content_type = request.headers.get('Content-Type')
    pls = [b.serialize() for b in db1.view()]
    if (content_type == 'application/json'):
        json = request.json
        print(json)
        for b in pls:
            if b['id'] == int(json['id']):
                return jsonify({
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting all Playlists!'
                })
        return jsonify({
            'error': f"Error ! Playlists with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': pls,
                    'status': '200',
                    'msg': 'Success getting all playlists in library!',
                    'no_of_songs': len(pls)
                })


@app.route('/songs', methods=['GET'])
def getRequest():
    # db.connect()
    content_type = request.headers.get('Content-Type')
    sgs = [b.serialize() for b in db.view()]
    
    if (content_type == 'application/json'):
        json = request.json
        print(json)
        for b in sgs:
            if b['id'] == int(json['id']):
                return jsonify({
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting all Songs!'
                })
        return jsonify({
            'error': f"Error ! Songs with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    # 'error': '',
                    'res': sgs,
                    'status': '200',
                    'msg': 'Success getting all songs in library!',
                    'no_of_songs': len(sgs)
                })

@app.route("/songs", methods=['POST'])
def postRequest():
    
    req_data=request.get_json()
    title = req_data['title']
    album= req_data['album']
    artist=req_data['artist']
    sg = [b.serialize() for b in db.view()]
    for b in sg:
        if b['title'] == title:
            return jsonify({
                'res': f'Error ! song with title {title} is already in library!',
                'status': '404'
            })

    Sg = Song(db.getNewId(),title,album,artist)
    print('new song: ', Sg.serialize())
    db.insert(Sg)
    new_songs = [b.serialize() for b in db.view()]
    print('Songs: ', new_songs)
    
    return jsonify({
                'res': Sg.serialize(),
                'status': '200',
                'msg': 'Success creating a new song!'
            })

@app.route('/songs/<id2>', methods=['GET'])
def getRequestId(id2):
    req_args = request.view_args
    print('req_args: ', req_args)
    sgs = [b.serialize() for b in db.view()]
    if req_args:
        for b in sgs:
            if b['id'] == int(req_args['id2']):
                return jsonify({
                    # 'error': '',
                    'res': b,
                    'status': '200',
                    'msg': 'Success getting song by ID !'
                })
        return jsonify({
            'error': f"Error! Song with id '{req_args['id2']}' was not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    'res': sgs,
                    'status': '200',
                    'msg': 'Success getting song by ID!👍😀',
                    'no_of_songs': len(sgs)
                })

@app.route('/songs/<id>', methods=['DELETE'])
def deleteRequest(id):
    req_args = request.view_args
    print('req_args: ', req_args)
    sgs = [b.serialize() for b in db.view()]
    if req_args:
        for b in sgs:
            if b['id'] == int(req_args['id']):
                db.delete(b['id'])
                updated_sgs = [b.serialize() for b in db.view()]
                print('updated_sgs: ', updated_sgs)
                return jsonify({
                    'res': updated_sgs,
                    'status': '200',
                    'msg': 'Success deleting song by ID!',
                    'no_of_songs': len(updated_sgs)
                })
            
        return jsonify({
            'error': f"Error ! Wrong song ID sent!",
            'res': '',
            'status': '404'
           })

    else:
        return jsonify({
            'error': f"Error ! No song ID sent!",
            'res': '',
            'status': '404'
        })

@app.route('/delete_all_songs', methods=['DELETE'])
def deleteall():
    db.deleteAll()
    sgs = [b.serialize() for b in db.view()]
    return jsonify({
        'res': sgs,
        'status': '200',
        'msg': 'Success deleting song by ID!',
        'no_of_songs': len(sgs)
        })





if __name__ == '__main__':
    app.run()