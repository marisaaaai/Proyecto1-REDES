#######################################################
# Redes Clase 
# Proyecto 1
# Protocolo XXP principal 
# María Montoya
# #19169 :)
#######################################################
import logging
import time
import sleekxmpp
from getpass import getpass
from prettytable import PrettyTable
from sleekxmpp.exceptions import IqError, IqTimeout

import cliente
from consts import *

close_login = False

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)-8s %(message)s')


# With tkinter, opens a windows for the user to select a file.
def get_file_path():
    file_path = filedialog.askopenfilename()
    return file_path


# Prints a table with all of the groups the user is part of
def print_groups(group_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}No.{ENDC}',
                         f'{BOLD}ROOM{ENDC}',
                         f'{BOLD}NICK{ENDC}']

    table.align = 'l'
    counter = 1
    for url, group in group_dict.items():
        group_info = group.get_data()
        table.add_row([counter, group_info[0], group_info[1]])
        counter += 1

    print(table)


# Prints a table with every user and its index
def print_contact_index(user_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}No. {ENDC}',
                         f'{BOLD}USERNAME{ENDC}',
                         f'{BOLD}SHOW{ENDC}',
                         f'{BOLD}JID{ENDC}']
    table.align = 'l'
    counter = 1
    for jid, user in user_dict.items():
        user_info = user.get_connection_data()
        table.add_row([counter, user_info[0], user_info[1], jid])
        counter += 1

    print(table)


# Prints all users through a table
def print_all_users(user_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}USERNAME{ENDC}',
                         f'{BOLD}NAME{ENDC}',
                         f'{BOLD}EMAIL{ENDC}',
                         f'{BOLD}JID{ENDC}']
    table.align = 'l'
    for jid, user_info in user_dict.items():
        table.add_row([user_info[0], user_info[1], user_info[2], jid])

    print(table)


# Prints a table with every contact and its connection data
def print_contacts(user_dict):
    table = PrettyTable()
    table.field_names = [f'{BOLD}USER{ENDC}',
                         f'{BOLD}SHOW{ENDC}',
                         f'{BOLD}STATUS{ENDC}',
                         f'{BOLD}SUBSCRIPTION{ENDC}',
                         f'{BOLD}JID{ENDC}']
    table.align = 'l'
    for jid, user in user_dict.items():
        user_data = user.get_connection_data()
        user_data.append(jid)
        table.add_row(user_data)

    table.sortby = f'{BOLD}SHOW{ENDC}'
    print(table)


# Prints a table with every user and its connection data
def print_user_data(users, amount):
    table = PrettyTable(border=False)
    table.field_names = [f'{BOLD}EMAIL{ENDC}',
                         f'{BOLD}JID{ENDC}',
                         f'{BOLD}USERNAME{ENDC}',
                         f'{BOLD}NAME{ENDC}']
    table.align = 'l'
    counter = 0
    user_data = []
    for data in users:
        counter += 1
        user_data.append(data)
        if counter % 4 == 0:
            table.add_row(user_data)
            user_data = []

    print(table)


# Hanldes the client once the user logged in
def handle_session(event):
    close_session = False
    xmpp.session_start()
    option = ''
    print(f'{OKGREEN}Logged in as {xmpp.boundjid.bare}{ENDC}')

    while not close_session:
        print(main_menu)
        option = input('Enter an option: ')

        # OPTION 1: Show connected users
        if option == '1':

            print(
                f'\n{BLUE}|================================================|{ENDC}')
            print(f'\n{BOLD}My roster:{ENDC}\n')
            roster = xmpp.get_user_dict()
            print_contacts(roster)

        # OPTION 2: Add a user to my contact list
        elif option == '2':
            print(f'\n{BOLD}Add user to contact list{ENDC}')
            user_jid = input('Enter user jid: ')

            if user_jid and '@' in user_jid:
                xmpp.add_user(user_jid)
            else:
                print(invalid_option)

        # OPTION 3: Get user details
        elif option == '3':
            username = input('Enter a username to search: ')

            user_data, amount = xmpp.get_user_data(username)

            if not user_data:
                print(f'{RED}User not found...{ENDC}')
            else:
                print_user_data(user_data, amount)

        # OPTION 4: Private session
        elif option == '4':
            print(f'\n{BOLD}Send a private message{ENDC}\n')
            # Get updated roster
            roster = xmpp.get_user_dict()

            # Get all users as list
            users = list(roster.keys())

            # Print table of users with their index
            print_contact_index(roster)
            recipient = input('\nEnter recipient index or jid: ')

            if '@' in recipient:
                dest = recipient

            else:
                try:
                    recipient = int(recipient)
                    # Check if user index was correct
                    dest = users[recipient-1]
                except ValueError:
                    # Else, repeat
                    print(invalid_option)
                    continue

            received_messages = roster[dest].get_messages()
            if received_messages:
                print(
                    f'\n{YELLOW}The message(s) with {dest} are:{ENDC}')
                for sender, msg in received_messages:
                    print(f'\t{sender}:  {msg}')

            new_message = input('\nEnter a message: ')
            xmpp.send_session_message(dest, new_message)

        # OPTION 5: Group chat options
        elif option == '5':

            print(group_options)

            group_option = input('\tEnter an option: ')

            # 1. Create a group
            if group_option == '1':
                print(f'\n{BOLD}Funcionalidad no creada{ENDC}')
                

            # 2. Join a group
            elif group_option == '2':
                print(f'\n{BOLD}Join a group chat{ENDC}')

                room = input('Room URL: ')
                nick = input('Nick: ')

                if nick and room:
                    xmpp.join_room(room, nick)
                    print(f'{OKGREEN}Joined {room}{ENDC}')
                else:
                    print(f'{FAIL}Please set a group name and a nick{ENDC}')
                    continue

            # 3. Send message to a group
            elif group_option == '3':

                print(f'\n{BOLD}Send a message to a group{ENDC}')
                room_dict = xmpp.get_group_dict()

                if room_dict:
                    # Print table of groups with their index
                    print_groups(room_dict)
                    recipient = input('\nEnter recipient index or jid: ')

                    if '@' in recipient:
                        dest = recipient
                    else:
                        try:
                            recipient = int(recipient)
                            # Check if user index was correct
                            dest = list(room_dict.keys())[recipient-1]
                        except ValueError:
                            # Else, repeat
                            print(invalid_option)
                            continue

                    received_messages = room_dict[dest].get_messages()
                    if received_messages:
                        print(
                            f'\n{YELLOW}The message(s) from {dest} are:{ENDC}')
                        for sender, msg in received_messages:
                            print(f'\t{sender} --> {msg}')

                    new_message = input('\nEnter a message: ')

                    if new_message:
                        if xmpp.send_groupchat_message(dest, new_message):
                            print(f'{OKGREEN}Message sent!{ENDC}')
                        else:
                            print(error_msg)

                else:
                    print(f'{FAIL}You havent joined any room yet.{ENDC}')

            # 4. Leave group
            elif group_option == '4':
                print(f'\n{BOLD}Leave room{ENDC}')
                room = input('Room URL: ')
                nick = input('Nick: ')

                if room and nick:
                    xmpp.leave_room(room, nick)
                    print(f'{OKGREEN}You left the group.{ENDC}')
                else:
                    print(f'{FAIL}You must provide a nick and a room!{ENDC}')
                    continue

            # 5. Cancel
            elif group_option == '5':
                continue

            # Invalid option
            else:
                print(invalid_option)

        # OPTION 6: Presence message
        elif option == '6':
            print(f'\n{BOLD}Presence message{ENDC}')
            print(show_options)

            # Let user decide his options
            show_input = input('Show: ')
            status = input('Status: ')

            try:
                # Validate if user selected a valid option
                show = show_array[int(show_input)-1]
            except:
                # If not, go to the default one.
                print(
                    f'{WARNING}Incorrect show option selected... Seting show to "available".')
                show = 'available'

            # Send the presence message and inform the user about it.
            xmpp.presence_message(show, status)
            print(f'{OKGREEN}Presence message sent!{ENDC}')

        # OPTION 7: Send a file
        elif option == '7':
            print(f'{BOLD}funcionalidad no realizada :({ENDC}')
            

        # OPTION 8: Log out.
        elif option == '8':
            print(f'\n{BOLD}Logging out of {xmpp.boundjid.bare}{ENDC}')
            xmpp.disconnect()
            close_session = True

        # OPTION 9: Delete account from server.
        elif option == '9':
            print(f'\n{WARNING}Deleting account: {xmpp.boundjid.bare}{ENDC}')
            xmpp.delete_account()
            xmpp.disconnect()
            close_session = True

        else:
            print(invalid_option)


if __name__ == "__main__":

    while not close_login:

        print(login_menu)
        option = input('Enter an option: ')

        # Register a new user
        if option == '1':
            print('\nRegister a new account')
            username = input('Enter your jid: ')
            password = getpass('Enter your password: ')

            if username and password:
                print(
                    f'{WARNING}Initiating registration process... please wait.{ENDC}')
                xmpp = cliente.RegisterBot(username, password)
                xmpp.register_plugin('xep_0030')  # Service Discovery
                xmpp.register_plugin('xep_0004')  # Data forms
                xmpp.register_plugin('xep_0066')  # Out-of-band Data
                xmpp.register_plugin('xep_0077')  # In-band Registration
                xmpp.register_plugin('xep_0045')  # Groupchat
                xmpp.register_plugin('xep_0199')  # XMPP Ping
                xmpp['xep_0077'].force_registration = True

                if xmpp.connect():
                    xmpp.process(block=True)
                else:
                    print(f'{FAIL}Unable to connect to the server{ENDC}')
            else:
                print(f'{FAIL}Input is incorrect.')

        # Login with credentials
        elif option == '2':
            print(f'\n{BOLD}Login in to your account{ENDC}')
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')

            if not username or not password:
                print(f'{FAIL} please enter a username and a password!{ENDC}')
                continue

            xmpp = cliente.Client(username, password)

            xmpp.add_event_handler(
                "session_start", handle_session, threaded=True)
            if xmpp.connect():
                xmpp.process(block=False)
                close_login = True
            else:
                print(f'{FAIL}Unable to connect to the server{ENDC}')
                xmpp.disconnect()
                continue

        elif option == '3':
            print('Exiting the program...')
            close_login = True

        else:
            print(invalid_option)