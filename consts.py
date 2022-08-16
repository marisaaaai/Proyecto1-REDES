HEADER = ""
OKBLUE = 'OK: '
OKGREEN = 'OK: '
WARNING = 'WARNING: '
FAIL = 'FAIL: '
ENDC = ''
BOLD = ''
UNDERLINE = ''
BLUE = ''
RED = ""
YELLOW = ''
# Menu messages
login_menu = f"""
{HEADER} LOGIN MENU {ENDC}
1. Crear una nueva cuenta
2. Ingresar a tu cuenta
3. Salir
{HEADER}{ENDC}
"""

main_menu = f"""
{HEADER}MAIN MENU {ENDC}
1. Mostrar  todos los contactos
2. Agregar usuario a los contactos
3. Mostrar detalles de un usuario
4. Chat privado
5. Participar en conversaciones grupales
6. Definir mensaje de presencia
7. Enviar / recibir archivos
8. Log out
9. Borrar mi cuenta del servidor 
{HEADER}{ENDC}
"""

group_options = f"""
\tSelect one of the options below:
\t1. Crear chat grupal
\t2. Unirse a un chat grupal
\t3. enviar mensaje 
\t4. salir del chat grupal
\t5. Cancel
"""

show_options = f"""
Select one of the options below:
1. chat
2. away
3. xa (eXtended away)
4. dnd (do not disturb)
"""

# Errors messages
error_msg = f"""
{FAIL}Something went wrong...{ENDC}
"""
invalid_option = f'{FAIL}please enter a valid option!{ENDC}'

chat_session = f"""
********************************************************
|        YOUR ARE NOW IN A PRIVATE CHAT SESSION        |
********************************************************

Type {BOLD}exit{ENDC} to leave this chat session.
"""

# Userful variables
show_array = ['chat', 'away', 'xa', 'dnd']

# NOTIFICATIONS:
NEW_MESSAGE = '''
|==============> NEW MESSAGE <==============|
'''

FILE_OFFER = '''
<==============| OFFERED FILE |==============>
'''

SUSCRIPTION = '''
|==============| SUSCRIPTION |==============|
'''

GOT_ONLINE = '''
|==============> NOW ONLINE <==============|
'''

GROUPCHAT = '''
|==============>  GROUP CHAT <==============|
'''

STREAM_TRANSFER = '''
|==============> STREAM STARTED <==============|
            File transfer initiated!

Please wait...
'''