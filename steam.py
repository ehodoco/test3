from funcs import login, print_menu, ingresar_dinero, juegos_aptos, print_lista_juegos, precio_carrito

autenticado=False
usuario = login()

if usuario != None:
    autenticado = True
    lista_juegos = juegos_aptos(usuario)
    juegos_usuario = []
    carrito = []
    print()

while autenticado:
    
    print_menu(lista_juegos)

    print(f"Actualmente tienes {usuario.saldo}€")
    print("--------------------------------")
    print("[V]er mis juegos")
    print("[I]ngresar dinero")
    print("Ir al [C]arrito")
    print("[S]alir")

    input_usuario=input("¿Que quieres hacer? ").lower()
    print("--------------------------------")

    if input_usuario == "v":
        print("Tienes los siguientes juegos:")
        print_lista_juegos(juegos_usuario)

    elif input_usuario == "i":
        dinero_ingresar = ingresar_dinero()
        print(f"Enhorabuena has ingresado {dinero_ingresar}€")
        usuario.saldo += dinero_ingresar

    elif input_usuario == "c":
        print("Tienes los siguientes juegos en el carrito:")
        total_carrito = precio_carrito(carrito)
        print("[P]agar")
        print("[V]olver")
        opcion_comprar = input().lower()

        if opcion_comprar == "p":
            if usuario.saldo >= total_carrito:
                usuario.saldo -= total_carrito
                juegos_usuario.extend(carrito)
                carrito.clear()
                print("Gracias por tu compra")
            else:
                print("Saldo insuficiente")
            
    elif input_usuario == "s":
        break

    else:
        try:
            int_input_usuario = int(input_usuario)-1
            lista_juegos[int_input_usuario]
        except:
            print("\n Opción no válida")
        else:
            print(f"\n{lista_juegos[int_input_usuario]}")
            opcion_anhadir_carrito = input("¿Quieres añadir el juego al carrito? (S/N) ").lower()

            if opcion_anhadir_carrito == "s":
                carrito.append(lista_juegos[int_input_usuario])
                lista_juegos.pop(int_input_usuario)
    
    input()

