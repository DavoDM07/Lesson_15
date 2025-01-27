#Write a simple login system where the user enters a username and password. Handle
#the KeyError by raising a custom exception if the username is not found in the users
#database(dictionary).

list_of_users = {'sergey':'qwerty123','simon':'123simon123','sahak':'password123','lilit':'lilit_123'}
username = input('Enter username >>> ')
user_password = input('Enter password >>> ')

if username in list_of_users:
    if list_of_users[username] == user_password:
        print('Successful Login')
    else:
        print('Wrong password')
else:
    raise KeyError('Wrong username')