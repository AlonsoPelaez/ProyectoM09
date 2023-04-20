import requests, json


def mostrar_menu(nombre, opciones):
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (opcionSelecionada := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return opcionSelecionada


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Grupos >', submenuGrupos),
        '2': ('Albums >', submenuAlbums),
        '3': ('Canciones >', submenuCanciones),
        '4': ('Salir', salir)
    }

    generar_menu('Menú principal', opciones, '4')


# sub menu de grupos
def submenuGrupos():
    opciones = {
        'a': ('Ver Grupos', show_grupos),
        'b': ('Editar Grupo', modify_grupo),
        'c': ('Añadir nuevo Grupo', add_grupo),
        'd': ('Eliminar Grupo', delete_grupo),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')


# sub menu de albums
def submenuAlbums():
    opciones = {
        'a': ('Ver Albums', show_albums),
        'b': ('Editar Album', modify_album),
        'c': ('Añadir nuevo Album', add_album),
        'd': ('Eliminar Album', delete_album),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')


#  sub menu de canciones
def submenuCanciones():
    opciones = {
        'a': ('Ver Canciones', get_canciones),
        'b': ('Editar Cancion', modify_cancion),
        'c': ('Añadir nueva Cancion', add_cancion),
        'd': ('Eliminar Cancion', delete_cancion),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')


# funcion get grupos funcional
def show_grupos():
    grupos = requests.get('http://127.0.0.1:5000/groups/')  # hacemos la peticion del servidor de los grupos disponibles
    data = grupos.json()  # convertimos el response de la peticion a json
    print("---------------------")
    print("        GRUPOS")
    print("---------------------")
    print("ID " + "    NAME ")
    print("---------------------")
    for grupo in data:  # hacemos un bucle de los grupos disponibles en el servidor
        print(grupo["id"], "  ", grupo["name"])  # imprime grupo
    print("---------------------")


# funcion delete grupo funcional
def delete_grupo():
    print("------------------------")
    print("  ELIMINAR GRUPO")
    show_grupos()  # muestra grupos
    idGroup = input('Introduzca el id del grupo: ')  # solicita un id al usuario

    while not idGroup.isdigit():  # verifica si el id es un entero
        idGroup = input(
            "Introduzca solo numeros para el id del grupo: ")  # si idGroup no es un entero vuelve a solicitar el id

    response = requests.get(
        'http://127.0.0.1:5000/groups/' + idGroup)   # hacemos la peticion al servidor para que retorne el grupo con el id proporcionado

    if response.status_code == 404:   # verifica si el response de la peticion devuelve 404 el id del grupo no existe
        print('ID inexistente, Vuelva a intentarlo!')
    else:
        try:
            borra_grupo = requests.delete(
                'http://127.0.0.1:5000/groups/' + idGroup)  # hacemos la accion de borrado junto con el idGroup
            print(borra_grupo.status_code)  # imprime el estado de la operacion
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el grupo:', e)


# funcion de modicar grupo funcional
def modify_grupo():
    print("---------------------")
    print("   MODIFICA GRUPOS")
    show_grupos()  # muestra grupos
    idGroup = input('Introduzca el id del grupo: ')  # solicita un id al usuario
    while not idGroup.isdigit():  # verifica si el id es un entero
        idGroup = input("Introduzca solo numeros para el id del grupo: ")  # si idGroup no es un entero vuelve a solicitar el id

    response = requests.get(
        'http://127.0.0.1:5000/groups/' + idGroup)  # hacemos la peticion al servidor para que retorne el grupo con el id proporcionado

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404 el id del grupo no existe
        print('ID inexistente, Vuelva a intentarlo!')
    else:
        nombre = input("nuevo nombre del grupo: ") #solicita nombre al usuario
        try:
            json_grupo = {"name": nombre} #estructuramos el json a partir de la informacion recibida
            modifica_grupo = requests.put('http://127.0.0.1:5000/groups/' + idGroup, json=json_grupo)  # hacemos accion de modificado junto con el idGroup y el json del grupo
            print(modifica_grupo.status_code)  # imprim el estado de la operacion
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el grupo:', e)


# funcion add grupos funcional
def add_grupo():
    print("------------------------")
    print("  AÑADE UN NUEVO GRUPO")
    print("------------------------")
    nombre = input("Introduzca el nombre del grupo: ")  # solicita el nombre del grupo al usuario

    try:
        grupo = {"name": nombre}  # estructura el json a partir de los valores brindados por el usuario
        agrega_grupo = requests.post('http://127.0.0.1:5000/groups/',
                                     json=grupo)  # hace el envio del json al servidor mediante el post
        print(agrega_grupo.status_code)  # imprime el estado de la operacion del envio del json
    except requests.exceptions.HTTPError as e:
        print('Error al eliminar el grupo:', e)


# albums

# funcion de get album funcional
def show_albums():
    albums = requests.get('http://127.0.0.1:5000/albums/')  # hacemos la peticion de albums al servidor
    data = albums.json()  # convertimos el response de la peticion al servidor a json
    print("---------------")
    print("  ALBUMS")
    print("---------------")
    for album in data:
        # imprime album
        print("'ID'", album["id"])
        print("'GROUP'", album["group"])
        print("'TITLE'", album["title"])
        print("'IMAGE'", album["image"])
        print("'DESCRIPTION'", album["description"])
        print("---------------")


# funcion borra album funcional
def delete_album():
    print("------------------------")
    print("  ELIMINAR ALBUM")
    show_albums()  # muestra los albums disponibles
    idAlbum = input('Introduzca el id del album: ')  # peticion de id al usuario
    while not idAlbum.isdigit():  # comprobamos que el id del album sea entero
        idAlbum = input(
            "Introduzca solo numeros para el id del album: ")  # hacemos la peticion al servidor para que retorne el album con el id proporcionado

    response = requests.get(
        'http://127.0.0.1:5000/albums/' + idAlbum)  # hacemos la peticion al servidor de grupos disponibles

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404 el id de album no existe
        print('ID inexistente, Vuelva a intentarlo!')
    else:
        try:
            borra_album = requests.delete(
                'http://127.0.0.1:5000/albums/' + idAlbum)  # hacemos la accion de borrado al servidor con el id del album
            print(borra_album.status_code)  # imprime el estado de la operacion
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el album:', e)


# funcion modificar album funcional
def modify_album():
    albums = requests.get('http://127.0.0.1:5000/albums/')  # hacemos la peticion al servidor de grupos disponibles
    data = albums.json()  # convertimos el response de la peticion a json

    print("---------------------")
    print("   MODIFICA ALBUM")
    print("---------------------")
    print("ID      TITLE")
    print("---------------------")
    for album in data:  # bucle de los grupos disponibles en el servidor
        print(album["id"], album["title"]) #imptimr album
        print("---------------------")

    idAlbum = input('Introduzca el id del album: ')  # solicita un id al usuario
    while not idAlbum.isdigit():  # verifica si el id es un entero
        idAlbum = input(
            "Introduzca solo numeros para el id del album: ")  # si idAlbum no es un entero vuelve a solicitar el id

    response = requests.get(
        'http://127.0.0.1:5000/albums/' + idAlbum)  # hacemos la peticion al servidor para que retorne el album con el id proporcionado

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404 el id del album no existe
        print('ID inexistente, Vuelva a intentarlo!')

    else:
        # formulario de modificado
        title = input("Introduce el nuevo titulo : ")
        image = input("Introduce una nuevaimagen : ")

        show_grupos()  # muestra grupos

        idGroup = input("Introduce el id del grupo: ")
        while not idGroup.isdigit():  # verifica si el id es un entero
            idGroup = input(
                "Introduzca solo numeros para el id del grupo: ")  # si idGroup no es un entero vuelve a solicitar el id

        response = requests.get(
            'http://127.0.0.1:5000/groups/' + idGroup)  # hacemos la peticion al servidor de grupos disponibles
        if response.status_code == 404:
            idGroup = input("ID inexistente, Introduzca el id del grupo: ")

        description = input("Introduce la nueva descripcion: ")
        try:
            json_album = {"title": title, "image": image, "idGroup": idGroup,
                          "description": description}  # estructura el json
            modifica_album = requests.put('http://127.0.0.1:5000/albums/' + idAlbum,
                                          json=json_album)  # hacemos peticion de modificado junto con el idAlbum
            print(modifica_album.status_code)  # imprime el estado de la operacion
            print('El album con id', idAlbum, 'ha sido modificado exitosamente.')
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el grupo:', e)


# añadir album funcional
def add_album():
    print("------------------------")
    print("  AÑADE UN NUEVO ALBUM")
    print("------------------------")
    # peticion al usuario
    title = input("Introduzca el titulo: ")
    image = input("Introduzca la imagen: ")
    description = input("Introduzca la descripcion: ")

    if not title.strip() or not image.strip() or not description.strip():  # comprobamos campos vacios
        print("No puede haber campos vacios, Intentelo de nuevo!")
    show_grupos() #muestra grupos

    id_group = input("Introduzca el id del grupo: ") #solicita el id al usuario
    while not id_group.isdigit():  # verifica que el id del grupo sea un entero
        id_group = input(
            "Introduzca solo numeros para el id del grupo: ")  # si no es un entero vuelve hacer la peticion del id al usuario

    response = requests.get(
        'http://127.0.0.1:5000/groups/' + id_group)   # hacemos la peticion al servidor para que retorne el grupo con el id proporcionado

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404 el id del grupo no existe
        print('ID inexistente, Vuelva a intentarlo!')

    else:
        try:
            album = {"title": title, "image": image, "idGroup": id_group,
                     "description": description}  # estructuramos el json apartir de los valores brindados por el usuario
            agrega_album = requests.post('http://127.0.0.1:5000/albums/',
                                         json=album)  # hacemos el envio del json al servidor
            print(agrega_album.status_code)  # imprime el estado de la operacion
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el grupo:', e)


# canciones

# funcion get canciones funcional
def get_canciones():
    canciones = requests.get('http://127.0.0.1:5000/songs/')  # hacemos la peticion de canciones al servidor
    data = canciones.json()  # convertimos el response de la peticion a json
    print("------------------------------------------------------------------------")
    print("|                               CANCIONES                               |")
    print("------------------------------------------------------------------------")
    print("|ID          " + "ALBUM           " + "TITLE          " + "GROUP             " + "LENGTH   |")
    print("-------------------------------------------------------------------------")
    for cancion in data:  # bucle de las canciones disponibles en el servidor
        print(cancion["id"], " |", cancion["album"], " |", cancion["title"], " |", cancion["group"], " |",
              cancion["length"])  # imprime cancion
        print("------------------------------------------------------------------")


# funcion borra cancion funcional
def delete_cancion():
    print("------------------------")
    print("  ELIMINAR CANCION")
    get_canciones()  # hacemos la peticion de las canciones disponibles al servidor
    idCancion = input('Introduzca el id de la cancion: ')
    while not idCancion.isdigit():  # verificamos si el idCancion es entero
        idCancion = input(
            "Introduzca solo numeros para el id de la cancion: ")  # vuelve hacer la peticion del idCancion

    response = requests.get(
        'http://127.0.0.1:5000/songs/' + idCancion)  # hacemos la peticion al servidor para que retorne la cancion con el id proporcionado

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404 el id de la cancion no existe
        print('ID inexistente, Vuelva a intentarlo!')

    else:
        try:

            borra_cancion = requests.delete(
                'http://127.0.0.1:5000/songs/' + idCancion)  # hace la peticion de borrado con el id de la cancion
            print(borra_cancion.status_code)  # muestra el codigo de la operacin
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar la cancion:', e)


# funcion modificar  cancion funcional
def modify_cancion():
    albums = requests.get('http://127.0.0.1:5000/albums/')  # hacemos la peticion al servidor de grupos disponibles
    data = albums.json()  # convertimos el response de la peticion a json

    print("---------------------")
    print("   MODIFICA CANCION")
    print("---------------------")
    get_canciones() #muestra canciones

    idSong = input('Introduzca el id de la cancion: ')  # solicita un id al usuario
    while not idSong.isdigit():  # verifica si el id es un entero
        idSong = input(
            "Introduzca solo numeros para el id de la cancion: ")  # si idGroup no es un entero vuelve a solicitar el id

    response = requests.get(
        'http://127.0.0.1:5000/songs/' + idSong)  # hacemos la peticion al servidor para que retorne la cancion con el id proporcionado

    if response.status_code == 404:  # verifica si el response de la peticion devuelve 404, de lo contrario el id de la cancion no existe
        print('ID inexistente, Vuelva a intentarlo!')

    else:
        # formulario de modificad
        title = input("Introduce el nuevo titulo : ")
        length = input("Introduce la nueva duracion (mm:ss) : ")
        show_albums()
        idAlbum = input("Introduce el id del album: ")
        while not idAlbum.isdigit():  # verifica si el id es un entero
            idAlbum = input(
                "Introduzca solo numeros para el id del grupo: ")  # si idGroup no es un entero vuelve a solicitar el id

        response = requests.get(
            'http://127.0.0.1:5000/albums/' + idAlbum)  # hacemos la peticion al servidor para que retorne el album con el id proporcionado

        if response.status_code == 404:
            idAlbum = input("ID inexistente, Introduzca el id del album: ") # verifica si el response de la peticion devuelve 404, de lo contrarioel id del album no existe
        try:
            json_cancion = {"idAlbum": idAlbum, "title": title, "length": length} #estructura el json a partir de los datos proporcionados
            modifica_cancion = requests.put('http://127.0.0.1:5000/songs/' + idSong,
                                            json=json_cancion)  # hacemos peticion de modificado junto con el idAlbum y el json añadido
            print(modifica_cancion.status_code)  # imprime el estado de la operacion
            print('El album con id', idSong, 'ha sido modificado exitosamente.')
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar el grupo:', e)


# funcion add cancion funcional
def add_cancion():
    ids_albums = []  # crea array de id de los albums
    albums = requests.get('http://127.0.0.1:5000/albums/')  # peticion al servidor de albums disponibles
    data = albums.json()  # convierte el response de la peticion a un json

    print("------------------------")
    print("  AÑADE UN NUEVA CANCION")
    print("------------------------")
    print("     ALBUMS")
    print("------------------------")
    print("ID      TITLE ")
    print("------------------------")
    for album in data:
        # muestra albums disponibles para la seleccion de id del album al cual va a pertenecer
        ids_albums.append(album["id"])
        print(album["id"], album["title"])
        print("------------------------")

    # solcitamos parametros al usuarios
    idAlbum = input("Introduzca el id del Album: ")
    while not idAlbum.isdigit():  # comprobamos si el idAlbum es un entero
        idAlbum = input("Introduzca solo numeros para el id de la cancion: ")  # si no lo es vuelva a solicitar la id

    idAlbum = int(idAlbum)  # convertimos a integer
    while idAlbum not in ids_albums:  # verificamos si el id introducido existe
        print("el id de introducido no existe, Intentelo de nuevo")

    title = input("Introduzca el titulo: ")
    length = input("Introduzca la duracion (MM:SS) : ")

    if not title.strip() or not length.strip():  # comprobamos campos vacios
        print("No puede haber campos vacios, Intentelo de nuevo!")

    else:
        try:
            cancion = {"idAlbum": idAlbum, "title": title,
                       "length": length}  # estructuramos el json con los parametros solicitados
            agrega_cancion = requests.post('http://127.0.0.1:5000/songs/', json=cancion)  # hacemos el envio del json al servidor
            print(agrega_cancion.status_code)  # muestra el estado de la operacion en consola
        except requests.exceptions.HTTPError as e:
            print('Error al eliminar la cancion:', e)


def salir():
    print('Saliendo...')



if __name__ == '__main__':
    menu_principal()