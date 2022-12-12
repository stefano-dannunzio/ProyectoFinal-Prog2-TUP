#Importación de módulos - Import modules
from flask import Flask, jsonify, request

#Importación de Datos - Import Data
from users import users
from movies import movies



app = Flask(__name__)

#Autentificación usuario - Login user
@app.route('/ingresar_usuario', methods=['CONNECT']) 
def login_user():


#Agregar una reseña - Add a review
@app.route('/agregar_reseña', methods=['POST'])
def add_review():

#Agregar una pelicula - Add a movie
@app.route('/agregar_pelicula', methods=["POST"])
def add_movie():
    new_movie = {
        "Titulo": request.json['Titulo'], 
        "Anio": request.json ['Anio'], 
        "Director": request.json ['Director'], #En vez de pedirlo tendriamos que obtenerlo de la lista
        "Genero":  request.json ['Genero'], #En vez de pedirlo tendriamos que obtenerlo de la lista
        "Sinopsis":  request.json ['Sinopsis'], 
        "Imagen":  request.json ['Imagen']
    }

    movies.append(new_movie)
    print(request.json)
    return jsonify({"message":"Pelicula agregada con exito", "movies": movies})

#Borrar una pelicula - #Delete a movie
@app.route('/borrar_pelicula', methods=['DELETE'])
def delete_movie():
    