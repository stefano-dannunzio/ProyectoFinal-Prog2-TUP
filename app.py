#Importación de módulos - Import modules
from flask import Flask, jsonify, request, render_template
import json

#Importación de Datos - Import Data

from movies import movies

#Cargar el archivo users.json
with open('users.json', 'r') as f:
    users = json.load(f)

app = Flask(__name__)

#Numero de ID para peliculas
id = 0

#Inicio del sitio (modulo publico)
@app.route('/', methods=['GET'])
def index():
    #10 últimas peliculas cargadas
    latest_movies = []
    
    if id <= 0:
        return "No hay peliculas cargadas en la plataforma aún"

    elif id < 10:
        for movie in range(1, len(movies)+1):
            movie_dictionary = next((element for element in movies if element["ID"] == (movie)), None)
            latest_movies.append(movie_dictionary["Titulo"]) 
        
        return (latest_movies)
    else: 
        for movie in movies(id-10, id):
            movie_dictionary = next((element for element in movies if element["ID"] == movie), None)
            latest_movies.append(movie_dictionary["Titulo"]) 
            
        return (latest_movies)

print (index())


#Autentificación usuario - Login user
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



#Agregar una reseña - Add a review
@app.route('/agregar_reseña', methods=['POST'])
def add_review():
    
    return 0

#ABM de cada pelicula
#Agregar una pelicula - Add a movie
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

#Modificar una pelicula

#Borrar una pelicula - #Delete a movie
#@app.route('/borrar_pelicula', methods=['DELETE'])
#def delete_movie():

if __name__ == "__main__":
    app.run(debug=True)