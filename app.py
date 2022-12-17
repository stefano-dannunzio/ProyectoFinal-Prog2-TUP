# Importación de módulos - Import modules
from flask import Flask, jsonify, request, render_template, session
# from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
app.secret_key = 'tupsito'
# auth = HTTPBasicAuth()

# @auth.verify_password
# def verify_password(username, password):
#     with open('data/users.json') as f:
#         users = json.load(f)

#     if username in users and users[username] == password:
#         return True
#     return False

@app.route('/login', methods=['POST'])
def login():
    # Obtiene el usuario y contraseña de la request
    login_data = request.get_json()
    username = login_data['username']
    password = login_data['password']

    # Verificar el usuario y contraseña
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    if username in users and users[username] == password:
        # Guardar el username del usuario autenticado en la session
        session['username'] = username
        return jsonify({'message': 'Login con éxito'})
    else:
        return jsonify({'error': 'Usuario o contraseña invalido/a'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    # Limpia la variable de session "username"
    session.pop('username', None)
    return 'Log out satisfactorio', 200


@app.route('/register', methods=['POST'])
def register():
    # Obtener datos de la request
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Leer el users.json
    with open('data/users.json', 'r') as f:
        users = json.load(f)

    # Checkear si el nombre de usuario ya esta en uso
    if username in users:
        return 'Nombre de usuario ya en uso', 400

    # Añadir el usuario a la base de datos
    users[username] = password

    # Escribir la lista actualizada de usuarios al users.json
    with open('data/users.json', 'w') as f:
        json.dump(users, f)

    return 'Registrado con éxito', 201


# Ruta para el módulo publico
@app.route('/public', methods=['GET'])
def get_public_movies():
    # Cargar el archivo movies.json
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
    # Obtener las últimas 10 películas en la lista
    public_movies = movies[-10:]
    # Devolver las películas en JSON
    return jsonify(public_movies)

# ----- MODULOS PRIVADOS ---------

# Devolver lista de directores
@app.route('/directors', methods=['GET'])
def retrieve_directors():
    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    # Abrir el directors.json
    with open('data/directors.json', 'r') as f:
        directors = json.load(f)
    # Devolver los directores en JSON
    return jsonify(directors)

# Devolver lista de géneros
@app.route('/genres', methods=['GET'])
def retrieve_genres():
    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    # Abrir el genres.json
    with open('data/genres.json', 'r') as f:
        genres = json.load(f)
    # Devolver los géneros en JSON
    return jsonify(genres)


# Agregar una película
@app.route('/private/add', methods=['POST'])
def add_movie():
    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    # Obtener la información de la película desde la request
    movie_data = request.get_json()

    # Checkear que todos los campos requeridos estan presentes
    if 'title' not in movie_data or 'year' not in movie_data or 'director' not in movie_data or 'genre' not in movie_data or 'synopsis' not in movie_data or 'img_url' not in movie_data:
        return jsonify({'error': 'Falta/n campo/s requerido/s'}), 400

    # Obtener las listas de directores y géneros
    with open('data/directors.json', 'r') as f:
        directors = json.load(f)
    with open('data/genres.json', 'r') as f:
        genres = json.load(f)

    # Checkear si el director y el género son válidos
    if movie_data['director'] not in directors:
        return jsonify({'error': 'Director inválido'}), 400
    if movie_data['genre'] not in genres:
        return jsonify({'error': 'Género Inválido'}), 400

    # Añadir la película a la lista
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
    movie_added = False
    # Si la película ya se encuentra en la lista, simplemente se agrega la review a la lista de reviews
    for i, movie in enumerate(movies):
        if movie['title'] == movie_data['title'] and movie['year'] == movie_data['year']:
            movies[i]['reviews'].append(movie_data['review'])
            movie_added = True
            break
    # Si la película no se encuentra, se añade correctamente y se agrega la review
    # como primer elemento de la lista de reviews
    if not movie_added:
        movie_data['reviews'] = [movie_data['review']]
        del movie_data['review']
        movies.append(movie_data)
    with open('data/movies.json', 'w') as f:
        json.dump(movies, f)

    return jsonify({'message': 'Película agregada correctamente'}), 201



# Modificar una pelicula
@app.route('/private/modify/<string:title>', methods=['PUT'])
def update_movie(title):

    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401
    
    # Obtener los datos de la request
    movie_data = request.get_json()

    # Checkear que todos los datos estan presentes
    if 'year' not in movie_data or 'director' not in movie_data or 'genre' not in movie_data or 'synopsis' not in movie_data or 'img_url' not in movie_data:
        return jsonify({'error': 'Falta/n campo/s requerido/s'}), 400

    # Obtener las listas de directores y géneros
    with open('data/directors.json', 'r') as f:
        directors = json.load(f)
    with open('data/genres.json', 'r') as f:
        genres = json.load(f)

    # Checkear que el director y el género son válidos
    if movie_data['director'] not in directors:
        return jsonify({'error': 'Director inválido'}), 400
    if movie_data['genre'] not in genres:
        return jsonify({'error': 'Género inválido'}), 400

    # Actualizar la película en la lista
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
    for i, movie in enumerate(movies):
        if movie['title'] == title:
            movies[i]['title'] = movie_data['title']
            movies[i]['year'] = movie_data['year']
            movies[i]['director'] = movie_data['director']
            movies[i]['genre'] = movie_data['genre']
            movies[i]['synopsis'] = movie_data['synopsis']
            movies[i]['img_url'] = movie_data['img_url']
            break
    else:
        return jsonify({'error': 'Película no encontrada'}), 404
    with open('data/movies.json', 'w') as f:
        json.dump(movies, f)

    return jsonify({'message': 'Pelicula modificada satisfactoriamente'}), 200



# Agregar una reseña - Add a review
@app.route('/private/<string:movie>/agregar_reseña', methods=['PUT'])
def add_review(movie):

    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    #Cargar el archivo movies.json
    with open('json_files/movies.json', 'r') as f:
        movies = json.load(f)

    #Solicitar la reseña al usuario para luego almacenarla en la base de datos
    new_review =  request.json
    
    #Chequeamos que la reseña no este vacia
    if len(new_review) <= 0: 
        return jsonify({"El campo esta vacio. Por favor escriba una reseña para cargarla"})
    else:
        #Recorremos la lista de diccionarios para encontrar una coincidencia en base al titulo
        #Y agregar la reseña a ese titulo. 
        for i in movies:
            if i["title"] == movie:
                i["reviews"].append(new_review)

                #Devolver la base de datos actualizada
                with open ('data/movies.json', 'w') as f:
                    json.dump(movies, f)
                
        return jsonify({"message": "Reseña agregada con éxito", "movies": movies})



# Borrar una pelicula - #Delete a movie
@app.route('/private/<string:movie_delete>/borrar_pelicula', methods=['DELETE'])
def delete_movie(movie_delete):

    # Checkear si el usuario está autenticado
    if 'username' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    #Cargar el archivo movies.json
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)

    #Recorrer la lista de diccionarios para encontrar coincidencia con el nombre de la pelicula
    for movie in movies:
        if movie["title"] == movie_delete and len(movie["reviews"]) < 1:
            movies.remove(movie)
            
            #Devolver la base de datos actualizada
            with open ('data/movies.json', 'w') as f:
                json.dump(movies, f)

            return jsonify ({"message" : "Pelicula eliminada con éxito", "movies": movies})

        else:
            return jsonify ({"message" : "No se ha encontrado la pelicula o no se puede eliminar"})

if __name__ == "__main__":
    app.run(debug=True)