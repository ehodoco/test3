from funcs import *

autenticado = login()

while autenticado:
    print_menu()

    print(f"Actualmente tienes sero€")

    input_usuario=input()

    match input_usuario:
        case 1:
            die