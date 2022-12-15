#Importación de la libreria requests
import requests

#Importación de usuarios
from users import users

#Importación de películas
from movies import movies

#Mensaje de bienvenida
print('------------------ MoviesListManager v1.0 ------------------')
print("Por Marcia B. Álvarez, Stefano D'Annunzio y Pamela Dominguez")

#Menu de Autenticación
logged_in = False
print('¿Cómo quiere acceder al programa?')
print('---------------------------------')
print('1. COMO USUARIO REGISTRADO')
print('2. COMO INVITADO (Módulo público)')
print('---------------------------------')
option = input(print('Elija una opción: '))

match option:
    case 1:
        user = input(print('Ingrese su usuario: '))
        password = input(print('Ingrese su contraseña: '))
        if (user in users):
            if (password == users[user]):
                print('Hola,', user)
                logged_in = True
            else:
                print('Contraseña incorrecta.')
                print('Accederás al módulo público.')
        else:
            print('No existe ese usuario.')
            print('Accederás al módulo público.')


    case 2:
        print('Accederás al módulo público.')
    
if (logged_in == True):
    private_module()
else:
    public_module()


