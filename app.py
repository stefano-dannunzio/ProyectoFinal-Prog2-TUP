# Importación de módulos - Import modules
from flask import Flask, jsonify, request, render_template
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

# Importación de Datos - Import Data

# Cargar el archivo users.json
with open('users.json', 'r') as f:
    users = json.load(f)

# Cargar el archivo movies.json
with open('movies.json', 'r') as f:
    movies = json.load(f)

# Cargar el archivo directors.json
with open('directors.json', 'r') as f:
    directors = json.load(f)

# Cargar el archivo genres.json
with open('genres.json', 'r') as f:
    genres = json.load(f)

#Numero de ID para peliculas
#id = 0

# Autentificación usuario - Login user
@app.route('/login', methods=['POST'])
def login():
    # Obtener el usuario y la contraseña desde la request
    username = request.form['username']
    password = request.form['password']

    # Chequear si las credenciales provistas coinciden con un usuario en la lista de usuarios
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)
    if user:
        # Si son validas, retornan un mensaje satisfactorio
        return jsonify({'message': 'login successful'})
    else:
        # Si son invalidas, retornan un mensaje de error
        return jsonify({'message': 'invalid username or password'}), 401

# Definir una función para autenticar usuarios
@auth.verify_password
def verify_password(username, password):
    # Chequear si las credenciales provistas coinciden con un usuario en la lista de usuarios
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)
    if user:
        return True
    return False

# Ruta para el módulo publico
@app.route('/public')
def get_public_movies():
    # Obtener las últimas 10 películas en la lista
    public_movies = movies[-10:]
    # Devolver las películas en JSON
    return jsonify(public_movies)


# Ruta para el módulo privado
@app.route('/private', methods=['POST'])
@auth.login_required
def add_movie():
    # Get the movie data from the request
    data = request.get_json()

    # Chequear que los campos requeridos estan presentes
    if 'title' not in data or 'year' not in data or 'director' not in data or 'genre' not in data:
        return jsonify({'message': 'faltan campos requeridos'}), 400

    # Check that the director and genre are valid
    if data['director'] not in directors or data['genre'] not in genres:
        return jsonify({'message': 'director o género inválido/s'}), 401


# Agregar una reseña - Add a review
@app.route('/agregar_reseña', methods=['POST'])
def add_review():
    
    return 0

# ABM de cada pelicula
# Agregar una pelicula - Add a movie
@app.route('/agregar_pelicula', methods=["POST"])
def add_movie():
    #id += 1

    new_movie = {
        "Titulo": request.json['Titulo'], 
        "Anio": request.json ['Anio'], 
        "Director": request.json ['Director'], #En vez de pedirlo tendriamos que obtenerlo de la lista
        "Genero":  request.json ['Genero'], #En vez de pedirlo tendriamos que obtenerlo de la lista
        "Sinopsis":  request.json ['Sinopsis'], 
        "Imagen":  request.json ['Imagen'],
        "ID" : id + 1
    }

    movies.append(new_movie)
    id += 1
    print(request.json)
    return jsonify({"message":"Pelicula agregada con exito", "movies": movies})

# Modificar una pelicula

# Borrar una pelicula - #Delete a movie
#@app.route('/borrar_pelicula', methods=['DELETE'])
#def delete_movie():

if __name__ == "__main__":
    app.run(debug=True)