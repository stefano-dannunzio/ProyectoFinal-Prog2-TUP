#Importación de la libreria requests
import requests
import json
import maskpass

'''MENU INVITADO/USUARIO - REGISTRO'''
# --------------------------------------------------------------------
# VARIABLE GLOBAL PARA GUARDAR LA COOKIE DE AUTENTICACIÓN
COOKIE = None
# --------------------------------------------------------------------
# LOGIN
def login(username, password):
    global COOKIE
    data = {"username": username, "password": password}
    response = requests.post("http://localhost:5000/login", json=data)
    if response.status_code == 200:
        COOKIE = response.cookies
        print("Login satisfactorio.")
        return True
    else:
        print("Login fallido, chequee su usuario y/o contraseña.")
        return False
# --------------------------------------------------------------------
# LOGOUT
def logout():
    global COOKIE
    response = requests.post("http://localhost:5000/logout", cookies=COOKIE)
    if response.status_code == 200:
        COOKIE = None
        print("Logout satisfactorio.")
    else:
        print("Error: Quizás no hayas iniciado sesión")
# --------------------------------------------------------------------
# REGISTER
def register(username, password):
    data = {"username": username , "password": password}
    response = requests.post("http://localhost:5000/register", json=data)
    if response.status_code == 201:
        print('Te has registrado satisfactoriamente')
    else:
        print('Ha ocurrido un error')

# --------------------------------------------------------------------

def user_menu():    
    global COOKIE
    while COOKIE != None:
        print('---------------------------------')
        print('ABM - Alta Baja Modificación')
        print('---------------------------------')
        print('1. DAR DE ALTA UNA PELICULA')
        print('2. MODIFICAR UNA PELICULA')
        print('3. DAR DE BAJA UNA PELICULA')
        print('---------------------------------')
        print('OTRAS OPCIONES')
        print('---------------------------------')
        print('4. AGREGAR UNA RESEÑA')
        print('5. VER LISTA DE PELICULAS POR DIRECTOR ESPECIFICO')
        print('6. VER LISTA DE PELICULAS QUE TIENEN PORTADA')
        print('7. VER LISTA DE DIRECTORES')
        print('8. VER LISTA DE GÉNEROS')
        print('0. CERRAR SESIÓN')
        print('---------------------------------')
        option_menu = int(input("Elija una opción:"))
        match option_menu:
            case 1:
                print (f"Complete los datos pedidos a continuación para dar de alta una nueva pelicula:")

                new_title=""
                while len(new_title) <= 0:
                    new_title = str(input("Titulo de la pelicula: "))
                    if len(new_title) <= 0:
                        print (f"No puede continuar sin ingresar una pelicula")
                
                new_year=""
                while len(new_year) <= 0:
                    new_year = str(input("Año de lanzamiento: "))
                    if len(new_year) <= 0:
                        print (f"No puede continuar sin ingresar un año de lanzamiento")

                new_director=""
                while len(new_director) <= 0:
                    new_director = str(input("Director de la pelicula (Formato 'Apellido Nombre') según figura en la lista: "))
                    if len(new_director) <= 0:
                        print (f"No puede continuar sin ingresar un director")

                new_genre=""
                while len(new_genre) <= 0:
                    new_genre = str(input("Género (se acepta sólo uno, ingrese el más representativo de la lista): "))
                    if len(new_genre) <= 0:
                        print (f"No puede continuar sin ingresar un genero")

                new_synopsis=""
                while len(new_synopsis) <= 0:
                    new_synopsis = str(input("Sinopsis: "))
                    if len(new_synopsis) <= 0:
                        print (f"No puede continuar sin ingresar una sinopsis")

                new_img_url = ""
                while len(new_img_url) <= 0:
                    new_img_url = str(input("Link de la imagen: "))
                    if len(new_img_url) <= 0:
                        print (f"No puede continuar sin ingresar una imagen")

                new_reviews = str(input("Reseña: "))
                while len(new_reviews) <= 0:
                    new_reviews = str(input("Reseña: "))
                    if len(new_reviews) <= 0:
                        print (f"No puede continuar sin ingresar una reseña")
                
                print(add_movie(new_title, new_year, new_director, new_genre, new_synopsis, new_img_url, new_reviews))
                input("Presione enter para continuar... ")

                
            case 2:
                title_tobe_modified = input("¿Que pelicula desea modificar? Ingrese el titulo:")
                
                print("Ingrese los siguientes datos para actualizar la pelicula (Si un campo no cambia, ingreselo tal cual estaba previamente)")

                modified_title=""
                while len(modified_title) <= 0:
                    modified_title = str(input("Titulo de la pelicula: "))
                    if len(modified_title) <= 0:
                        print (f"No puede continuar sin ingresar una pelicula")
                
                modified_year = ""
                while len(modified_year) <= 0:
                    modified_year = str(input("Año de lanzamiento: "))
                    if len(modified_year) <= 0:
                        print (f"No puede continuar sin ingresar un año de lanzamiento")

                modified_director = ""
                while len(modified_director) <= 0:
                    modified_director = str(input("Director de la pelicula (Formato 'Apellido Nombre') según figura en la lista: "))
                    if len(modified_director) <= 0:
                        print (f"No puede continuar sin ingresar un director")
                
                modified_genre = ""
                while len(modified_genre) <= 0:
                    modified_genre = str(input("Género (se acepta sólo uno, ingrese el más representativo de la lista): "))
                    if len(modified_genre) <= 0:
                        print (f"No puede continuar sin ingresar un genero")
                
                modified_synopsis = ""
                while len(modified_synopsis) <= 0:
                    modified_synopsis = str(input("Sinopsis: "))
                    if len(modified_synopsis) <= 0:
                        print (f"No puede continuar sin ingresar una sinopsis")

                modified_img_url = str(input("URL a una imagen de la portada (*opcional): "))

                print(update_movie(title_tobe_modified, modified_title, modified_year, modified_director, modified_genre, modified_synopsis, modified_img_url))
                input("Presione enter para continuar... ")


            case 3:
                movie = str(input("Ingrese el título de la película que desea eliminar: "))
                print(delete_movie(movie))
                input("Presione enter para continuar... ")


            case 4:
                movie = input("Ingrese el nombre de la pelicula sobre la que quiere dejar una reseña: ")
                review = input("A continuación, ingrese su reseña de la pelicula: ")

                print(add_review(movie, review))
                input("Presione enter para continuar... ")


            case 5:
                directors_list()
                director = input("Ingrese el nombre del director sobre el cual quiere ver las peliculas, tal cual figura en la lista: ")
                
                get_movies_by_director(director)
                input("Presione enter para continuar... ")


            case 6:
                get_movies_with_poster()
                input("Presione enter para continuar... ")

            case 7:
                directors_list()
                input("Presione enter para continuar... ")

            case 8:
                genres_list()
                input("Presione enter para continuar... ")

            case 0:
                logout()
                input("Presione enter para continuar... ")

    
# --------------------------------------------------------------------
#ABM
''' ALTA DE UNA PELICULA '''
def add_movie(new_title, new_year, new_director, new_genre, new_synopsis, new_img_url=None, new_review=None):

    new_movie = {"title": new_title, "year": new_year, "director": new_director, "genre": new_genre, "synopsis": new_synopsis, "img_url": new_img_url, "review": new_review}
    response = requests.post("http://localhost:5000/private/add", json=new_movie, cookies=COOKIE)
    if response.status_code == 200:
        return ("Pelicula agregada con éxito")
    elif response.status_code == 401:
        return ("No autorizado")
    else:
        return ("Algo ha salido mal... intente nuevamente")

''' MODIFICACION DE UNA PELICULA '''
def update_movie(title_tobe_modified, modified_title, modified_year, modified_director, modified_genre, modified_synopsis, modified_img_url):
    global COOKIE

    updated_movie = {"title": modified_title, "year": modified_year, "director": modified_director, "genre": modified_genre, "synopsis": modified_synopsis, "img_url": modified_img_url}

    direction = (f"http://localhost:5000/private/modify/{title_tobe_modified}")
    response = requests.put(direction, json = updated_movie, cookies = COOKIE)

    if response.status_code == 201:
        return ("Pelicula modificada con éxito")
    elif response.status_code == 401:
        return ("No autorizado")
    else:
        return ("Algo ha salido mal... intente nuevamente")

''' BAJA DE UNA PELICULA '''
def delete_movie(movie_tobe_deleted):

    direction = (f'http://localhost:5000/private/{movie_tobe_deleted}/borrar_pelicula')
    print(direction)
    response = requests.delete(direction, cookies=COOKIE)
    if response.status_code == 200:
        return ("Pelicula eliminada con éxito")
    elif response.status_code == 401:
        return ("No autorizado")
    else:
        return ("Algo ha salido mal... intente nuevamente")
# --------------------------------------------------------------------
# AGREGAR UNA RESEÑA
def add_review(movie, new_review):
    global COOKIE
    
    if len(new_review) <= 0 or len(movie) <= 0:
        return ("La reseña o titulo de la pelicula estaban vacios, por favor intente nuevamente")

    direction = (f'http://localhost:5000/private/{movie}/agregar_reseña')
    response = requests.put(direction, json=new_review, cookies=COOKIE)
    if response.status_code == 201:
        return ("Reseña agregada con éxito")
    elif response.status_code == 400:
        return ("El campo esta vacio. Por favor escriba una reseña para cargarla")
    elif response.status_code == 401:
        return ("No autorizado")
     
    return ("Ha ocurrido un error, por favor intente nuevamente")
# --------------------------------------------------------------------
# DEVOLVER LISTA POR DIRECTOR ESPECIFICO
def get_movies_by_director(director):
    global COOKIE

    direction = (f'http://localhost:5000/private/movies_by/{director}')
    response = requests.get(direction, cookies=COOKIE)
    if response.status_code == 401:
        return("No autorizado")
    movies_by_director = response.json()

    
    print(f"La lista de peliculas del/la director/a {director} es:")
    contador_peliculas=1
    for movie in movies_by_director:
            print(f"{contador_peliculas}:")
            print(f"   Título : {movie['title']}")
            print(f"   Año de publicación : {movie['year']}")
            print(f"   Director : {movie['director']}")
            print(f"   Género : {movie['genre']}")
            print(f"   Sinopsis : {movie['synopsis']}")

            if len(movie['img_url']) > 0:
                print(f"   Link a imágen de la portada : {movie['img_url']}")
            else: 
                print(f"   Esta pelicula no cuenta con un link a una imagen de portada")
            
            if len(movie['reviews']) > 0:
                print(f"   Reseñas :")
                contadorReseñas = 1
                for review in movie['reviews']:
                    print(f"Reseñas {contadorReseñas}: {review}")
                    contadorReseñas += 1
            else:
                print (f"Esta pelicula no cuenta con reseñas aún.")
            
            contador_peliculas += 1
            print("--------------------------------------------")

# --------------------------------------------------------------------
# DEVOLVER LISTA DE PELICULAS CON PORTADA
def get_movies_with_poster():
    global COOKIE
    response = requests.get('http://localhost:5000/private/movies/with-images', cookies=COOKIE)
    
    if response.status_code == 401:
        return("No autorizado")
    
    movies_with_poster = response.json()
    
    print(f"Lista de peliculas con un poster cargado:")
    contador_peliculas=1
    for movie in movies_with_poster:
            print(f"{contador_peliculas}:")
            print(f"   Título : {movie['title']}")
            print(f"   Año de publicación : {movie['year']}")
            print(f"   Director : {movie['director']}")
            print(f"   Género : {movie['genre']}")
            print(f"   Sinopsis : {movie['synopsis']}")
            print(f"   Link a imágen de la portada : {movie['img_url']}")

            
            if len(movie['reviews']) > 0:
                print(f"   Reseñas :")
                contadorReseñas = 1
                for review in movie['reviews']:
                    print(f"Reseñas {contadorReseñas}: {review}")
                    contadorReseñas += 1
            else:
                print (f"Esta pelicula no cuenta con reseñas aún.")
            
            contador_peliculas += 1
            print("--------------------------------------------")

# --------------------------------------------------------------------
# DEVOLVER LISTA DE DIRECTORES
def directors_list():
    global COOKIE
    response = requests.get('http://localhost:5000/private/directors', cookies=COOKIE)
    if response.status_code == 401:
        return("No autorizado")
    directors = response.json()
    
    print(f"Lista de directores:")
    contador_directores=1
    for director in directors:
            print(f"{contador_directores}. {director}")
            contador_directores += 1

# --------------------------------------------------------------------
# DEVOLVER LISTA DE GENEROS
def genres_list():
    global COOKIE
    response = requests.get('http://localhost:5000/private/genres', cookies=COOKIE)
    if response.status_code == 401:
        return ("No autorizado")
    genres = response.json()
    
    print(f"Lista de generos:")
    contador=1
    for genre in genres:
            print(f"{contador}. {genre}")
            contador += 1

# --------------------------------------------------------------------

#Mensaje de bienvenida
print("------------------ MoviesListManager v1.0 ------------------")
print("Por Marcia B. Álvarez, Stefano D'Annunzio y Pamela Dominguez")

#Menu de Autenticación
while True:
    print('Bienvenidx al programa PelisPedia!')
    print('¿Qué desea realizar?')
    print('---------------------------------')
    print('1. OBTENER ULTIMAS 10 PELÍCULAS AGREGADAS')
    print('2. INICIAR SESION')
    print('--- Si desea salir, presione 3 ---')
    print('---------------------------------')
    option = int(input('Elija una opción y presione enter: '))

    match option:
        case 1:
            r = (requests.get("http://localhost:5000/public")).json()
            for movie in r:
                print(f"Título : {movie['title']}")
                print(f"Año de publicación : {movie['year']}")
                print(f"Director : {movie['director']}")
                print(f"Género : {movie['genre']}")
                print(f"Sinopsis : {movie['synopsis']}")

                if len(movie['img_url']) > 0:
                    print(f"Link a imágen de la portada : {movie['img_url']}")
                else: 
                    print(f"Esta pelicula no cuenta con un link a una imagen de portada")
                
                if len(movie['reviews']) > 0:
                    print(f"Reseñas :")
                    contadorReseñas = 1
                    for review in movie['reviews']:
                        print(f"Reseña {contadorReseñas}: {review}")
                        contadorReseñas += 1
                else:
                    print (f"Esta pelicula no cuenta con reseñas aún.")
                print("---------------------------------------")
        case 2:
            while True:
                if COOKIE == None:
                    print('---------------------------------')
                    print('1. INICIAR SESIÓN')
                    print('2. REGISTRARSE')
                    print('0. VOLVER AL MENU INICIAL')
                    print('---------------------------------')
                    option_menu_login = int(input("Elija una opcion:"))
                    match option_menu_login:
                        case 1:
                            username = input("Ingrese usuario:")
                            password = maskpass.askpass("Ingrese contraseña:", "*")
                            login(username, password)
                            user_menu()
                        case 2:
                            passwords_match = False
                            while passwords_match == False:
                                username = input("Ingrese usuario:")
                                password = maskpass.askpass("Ingrese contraseña:", "*")
                                confirm_password = maskpass.askpass("Ingrese nuevamente su contraseña:", "*")
                                if password == confirm_password:
                                    passwords_match = True
                                    register(username, confirm_password)

                                else:
                                    print('Las contraseñas no coinciden, intente nuevamente.')
                        case 0:
                            print('Gracias por usar esta herramienta, saludos!')
                            break

                        case _:
                            print('Debe elegir una opción correcta.')
                            
                else:
                    logged_out = False
                    while logged_out == False:
                        print('---------------------------------')
                        print('3. CERRAR SESIÓN')
                        print('---------------------------------')
                        option_menu_logout = int(input("Elija una opción:"))
                        if option_menu_logout == 3:
                            logout()
                            logged_out = True
                    break
        case 3:
            print('Gracias por usar esta herramienta, saludos!')
            break
        case _:
            print('Debes ingresar una opción incorrecta')
        
# --------------------------------------------------------------------

