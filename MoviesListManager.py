#Importación de la libreria requests
import requests

#Importación de usuarios
from users import users

#Importación de películas
from movies import movies

#--------------------------------------------------------------------

#Módulo privado
def private_module():
    print("privado")

#Módulo público
def public_module():
    print("publico")

    #Endpoint
    URL = ""

    #Request
    r = requests.get(URL)

    #Se extraen los datos de la request en formato JSON
    data = r.json()
    
    #Se muestran por consola las (ultimas 10 ) peliculas agregadas
    for i in range(1,10):
        print(data[-i])
        


#--------------------------------------------------------------------

#Mensaje de bienvenida
print("------------------ MoviesListManager v1.0 ------------------")
print("Por Marcia B. Álvarez, Stefano D'Annunzio y Pamela Dominguez")

#Menu de Autenticación
logged_in = False
print('¿Cómo quiere acceder al programa?')
print('---------------------------------')
print('1. COMO USUARIO REGISTRADO')
print('2. COMO INVITADO (Módulo público)')
print('---------------------------------')
option = int(input('Elija una opción: '))

if option == 1:
    
    user_input = input('Ingrese su usuario: ')
    password_input = input('Ingrese su contraseña: ')
    # --- CHEQUEO DE USUARIO Y CONTRASEÑA ---

    #Busqueda de usuario
    user = next((matching_user for matching_user in users if matching_user["user"] == user_input), None)

    #Chequeo por existencia de usuario
    if (user != None):
        #Chequeo por coincidencia de contraseña respectiva del usuario
        if (password_input == user["pass"]):
            print('Hola,', user["user"])
            logged_in = True
        else:
            print('ERROR: Contraseña incorrecta.')
            print('Accederás al módulo público.')
    else:
        print('ERROR: Usuario inexistente')
        print('Accederás al módulo público.')


else:
    print('Accederás al módulo público.')

    
if (logged_in == True):
    private_module()
else:
    public_module()


#-------------------------------------------



