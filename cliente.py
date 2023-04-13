import requests


# Obtenir la llista de groups
r = requests.get('http://127.0.0.1:5000/groups/')
print(r.status_code)
print(r.json())

# Obtenir un grup
r = requests.get('http://127.0.0.1:5000/groups/123')
print(r.status_code)
print(r.json())

# Crear un group
group = {"name": "The Velvet Underground"}
r = requests.post('http://127.0.0.1:5000/groups/', json=group)
print(r.status_code)

# Actualitzar un grup
group = {"name": "The Velvet Underground"}
r = requests.put('http://127.0.0.1:5000/groups/123', json=group)
print(r.status_code)

# Eliminar un grup
# r = requests.delete('http://127.0.0.1:5000/groups/123')
# print(r.status_code)