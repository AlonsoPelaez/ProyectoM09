from flask import *

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
    groups = db_music.get_groups(idGroup)

    if not groups:
        return {"error": "Group not found"}, 404

    if request.method == 'GET':
        return jsonify(groups[0])
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
        if not data["title"] or not data["image"] or not data["idGroup"] or not data["description"]:
            return {"error": " there are blank fields "}, 403

        group = db_music.get_groups(data["idGroup"])
        if group is None:
            return {"error": "idGroup does not exist"}, 403

        db_music.insert_album(data)
        return '', 201

@app.route('/songs/', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        songs = db_music.get_songs()
        return jsonify(songs)
    elif request.method == 'POST':
        data = request.json
        if not data["idAlbum"] or not data["title"] or not data["length"]:
            return {"error": "there are blank fields"}, 403
        db_music.insert_song(data)
        return '', 201

if __name__ == '__main__':
    app.run(debug=True)
