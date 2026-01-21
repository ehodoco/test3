from funcs import *

datos_login = login()
autenticado = datos_login[0]
usuario = datos_login[1]
del datos_login

while autenticado:
    print_menu()

    print(f"Actualmente tienes {usuario.saldo}€")

    input_usuario=input()

    match input_usuario:
        case 1:
            die