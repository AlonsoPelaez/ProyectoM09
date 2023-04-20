from flask import Flask, jsonify, request

import db_music

app = Flask(__name__)


@app.route('/groups/', methods=['GET', 'POST'])
def groups():
    if request.method == 'GET':
        groups = db_music.get_groups()
        return jsonify(groups)
    elif request.method == 'POST':
        data = request.json
        if not data["name"]:
            return {"error": "Name is empty"}, 403
        db_music.insert_group(data["name"])
        return '', 201

@app.route('/groups/<idGroup>', methods=["GET", "PUT", "DELETE"])
def group(idGroup):
    group= db_music.get_groups(idGroup)

    if not group:
        return {"error": "Group not found"}, 404

    if request.method == 'GET':
        return jsonify(group[0])
    elif request.method == 'PUT':
        data = request.json
        if not data["name"]:
            return {"error": "Name is empty"}, 403
        db_music.update_group(idGroup, data["name"])
        return {}
    elif request.method == 'DELETE':
        db_music.delete_group(idGroup)
        return {}

@app.route('/albums/', methods=['GET', 'POST'])
def albums():
    if request.method == 'GET':
        albums = db_music.get_albums()
        return jsonify(albums)
    elif request.method == 'POST':
        data = request.json

        group = db_music.get_groups(data["idGroup"])
        if group is None:
            return {"error": "idGroup does not exist"}, 403

        db_music.insert_album(data)

        return '', 201


@app.route('/albums/<idAlbum>', methods=["GET", "PUT", "DELETE"])
def album(idAlbum):
    album = db_music.get_albums(idAlbum)

    if not album:
        return {"error": "Album not found"}, 404

    if request.method == 'GET':
        return jsonify(album[0])

    elif request.method == 'PUT':
        data = request.json
        print(data)
        print(idAlbum)
        db_music.update_album(idAlbum, data)
        return {}
    elif request.method == 'DELETE':
        db_music.delete_album(idAlbum)
        return {}

@app.route('/songs/', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        songs = db_music.get_songs()
        return jsonify(songs)
    elif request.method == 'POST':
        data = request.json
        db_music.insert_song(data)
        return '', 201

@app.route('/songs/<idSong>', methods=["GET", "PUT", "DELETE"])
def song(idSong):
    song = db_music.get_songs(idSong)

    if not song:
        return {"error": "Song not found"}, 404

    if request.method == 'GET':
        return jsonify(song[0])

    elif request.method == 'PUT':
        data = request.json
        print(data)
        print(idSong)
        album = db_music.get_albums(data["idAlbum"])
        print(album)
        if album is None:
            return {"error": "IdAlbum does not exist"}, 403

        db_music.update_Songs(idSong, data)
        return {}
    elif request.method == 'DELETE':
        db_music.delete_song(idSong)
        return {}




if __name__ == '__main__':
    app.run(debug=True)