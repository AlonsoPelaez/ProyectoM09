import requests



def mostrar_menu(nombre, opciones):
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


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
        '1': ('Grupos', submenuGrupos),
        '2': ('Albums >', submenuAlbums),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Canciones', submenuCanciones),
        '4': ('Salir', salir)
    }

    generar_menu('Menú principal', opciones, '4')  # indicamos el nombre del menú

# sub menu de grupos
def submenuGrupos():
    opciones = {
        'a': ('Ver Grupos', get_grupos),
        'b': ('Editar Grupo', modify_grupo),
        'c': ('Añadir nuevo Grupo', ),
        'd': ('Eliminar Grupo', delete_grupo),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')

def submenuAlbums():
    opciones = {
        'a': ('Ver Grupos', get_albums),
        'b': ('Editar Grupo', modify_album),
        'c': ('Añadir nuevo Grupo', ),
        'd': ('Eliminar Grupo', delete_album),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')

def submenuCanciones():
    opciones = {
        'a': ('Ver Canciones', get_canciones),
        'b': ('Editar Cancion', modify_cancion),
        'c': ('Añadir nueva Cancion', ),
        'd': ('Eliminar Cancion', delete_grupo),
        'e': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'e')



# grupos
def get_grupos():
    print(" Grupos...")
    grupos = requests.get('http://127.0.0.1:5000/groups/')
    for grupo in grupos:
        print(grupo)

def delete_grupo():
    print("delete Grupos...")


def modify_grupo():
    print("Modificar Grupos...")


def add_grupo():
    print("Añadir Grupos...")

# albums

def get_albums():
    print("Albums...")


def delete_album():
    print("delete Albums...")


def modify_album():
    print("Modificar Albums...")

def add_album():
    print("add Albums...")





def get_canciones():

    print("Canciones...")


def delete_cancion():
    print("delete Cancion...")


def modify_cancion():
    print("Modificar Cancion...")


def add_cancion():
    print("add Albums...")


def salir():
    print('Saliendo...')




# Obtenir la llista de groups
# r = requests.get('http://127.0.0.1:5000/groups/')
# print(r.status_code)
# print(r.json())

# Obtenir un grup
# r = requests.get('http://127.0.0.1:5000/groups/123')
# print(r.status_code)
# print(r.json())

# Crear un group
# group = {"name": "The Velvet Underground"}
# r = requests.post('http://127.0.0.1:5000/groups/', json=group)
# print(r.status_code)

# Actualitzar un grup
# group = {"name": "The Velvet Underground"}
# r = requests.put('http://127.0.0.1:5000/groups/123', json=group)
# print(r.status_code)

# Eliminar un grup
# r = requests.delete('http://127.0.0.1:5000/groups/123')
# print(r.status_code)

if __name__ == '__main__':
    menu_principal()
