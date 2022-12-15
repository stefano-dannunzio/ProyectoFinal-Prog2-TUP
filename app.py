#Importación de módulos - Import modules
from flask import Flask, jsonify, request

#Importación de Datos - Import Data
from users import users
from movies import movies

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
@app.route('/login/<user>', methods=['GET']) 
def login_user(user, password):



#Agregar una reseña - Add a review
@app.route('/agregar_reseña', methods=['POST'])
def add_review():


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
@app.route('/borrar_pelicula', methods=['DELETE'])
def delete_movie():
