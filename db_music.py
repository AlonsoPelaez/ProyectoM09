import sqlite3


# get_groups() y get_group(idGroup) con CASI iguales
# se pueden juntar en una misma función combinada
#  para saber si hay o no parámetros se compara con 'None' (que es 'nada', 'vacio'

# al definir id=None se le esta diciendo a la función que el valor por defecto del
# parametro id será None
# si 'id' recibe un valor desde app.py tomara ése y NO None
def get_groups(idGroup=None):
    # se crea la conexion con la BD y se ejecuta la query
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'SELECT DISTINCT id, name FROM Groups'

    # Si hay un valor para 'id' entonces añadimos a la consulta
    # la clausula WHERE
    if idGroup is not None:
        # Esta es la única diferencia entre las dos funciones
        sql += ' WHERE id=' + idGroup

    cursor = conn.execute(sql)

    # se contruye una lista con un grupo  por fila
    # groups = [ {...grupo1...},{...grupo2...}]
    groups = []
    for row in cursor:
        # se crea un diccionario
        group = {}

        # cada campo del diccionario se debe llamar igual
        # que el del template donde se renderizará
        group['id'] = row[0]
        group['name'] = row[1]

        # se añade el grupo a la lista de grupos
        groups.append(group)
    # al final se cierra la conexion
    conn.close()

    # al final devolvemos los grupos
    return groups

def insert_group(name):
    # se crea la conexion con la BD y se ejecuta la query
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'INSERT INTO Groups (name) VALUES (?)'
    params = [name]

    conn.execute(sql, params)
    conn.commit()

    conn.close()

def update_group(id, name):
    # se crea la conexion con la BD y se ejecuta la query
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'UPDATE Groups SET name = ? WHERE id = ?'
    params = [name, id]

    conn.execute(sql, params)
    conn.commit()

    conn.close()

def delete_group(id):
    # se crea la conexion con la BD y se ejecuta la query
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'DELETE FROM Groups WHERE id = ?'
    params = [id]

    conn.execute(sql, params)
    conn.commit()

    conn.close()

# se da a idAlbum el valor por defecto None
def get_albums(idAlbum=None):
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'SELECT DISTINCT a.id, a.title, g.name, a.idGroup, a.description, a.image FROM Albums as a JOIN Groups as g ON (a.idGroup = g.id)'

    if idAlbum is not None:
        sql += ' WHERE a.id=' + idAlbum
    cursor = conn.execute(sql)
    albums = []
    for row in cursor:
        albums.append(
            {
                'id': row[0],
                'title': row[1],
                'group': row[2],
                'idGroup': row[3],
                'description': row[4],
                'image': row[5]
            })
    conn.close()
    return albums


def get_songs(idSong=None):
    sql = '''  
                SELECT s.id, s.title as cancion, s.length, a.title as album, g.name as grupo
                FROM Songs  as s JOIN Albums as a ON(s.idAlbum = a.id)
                JOIN Groups as g ON(a.idGroup = g.id)
            '''
    if idSong is not None:
        sql+= ' WHERE s.id=' + idSong
    print(sql)
    songs = []

    conn = sqlite3.connect('db_musica.sqlite')
    cursor = conn.execute(sql)
    for row in cursor:
        print('id:', row[0], '\tcancion:', row[1], ' \talbum:', row[2], '\tgrupo:', row[3])
        songs.append({
            'id': row[0],
            'title': row[1],
            'length': row[2],
            'album': row[3],
            'group': row[4]

        })
    conn.close()

    return songs


def insert_album(data):

        conn = sqlite3.connect('db_musica.sqlite')

        sql = 'INSERT INTO Albums (title, image, idGroup, description) VALUES (?,?,?,?)'
        params = [data["title"], data["image"], data["idGroup"], data["description"]]

        conn.execute(sql, params)
        conn.commit()

        conn.close()


def insert_song(data):
    # se crea la conexion con la BD y se ejecuta la query
    conn = sqlite3.connect('db_musica.sqlite')
    sql = 'INSERT INTO Songs (idAlbum, title, length) VALUES (?,?,?)'
    params = [data["idAlbum"], data["title"], data["length"]]

    conn.execute(sql, params)
    conn.commit()

    conn.close()