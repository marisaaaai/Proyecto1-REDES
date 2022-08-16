#######################################################
# Redes Clase 
# Proyecto 1
# Protocolo XXP
# María Montoya
# #19169 :)
#######################################################
from os import system, name
import getpass

def clr_scr():
    '''Clear Screen'''

    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def enter_to_continue():
    '''Press Enter to continue'''

    input("\nPresiona ENTER para continuar.")

def get_password():
    '''Get Password'''
    try:
        p = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        return p
    
    return None


def main_menu():
    '''Main Menu'''    
    return '''
    
    Proyecto #1

1. Registrarse
2. Iniciar Sesion
3. Salir
    '''

def login_menu():
    '''Login Menu'''

    return '''
    
    Inicia Sesion

    '''

def secondary_menu():
    '''Users Menu'''

    return '''
    
    Bienvenido a XMPP Chat

1. Mostrar todos los contactos
2. Agregar un usuario a tus contactos
3. Mostrar detalles de un usuario
4. Chats Personales
5. Chats Grupales
6. Definir Mensaje de Presencia
7. Enviar un archivo
8. Enviar notificaciones
9. Cerrar Sesion
00. Eliminar cuenta

    '''