from Videojuego import Videojuego
from datos import get_juegos, get_usuarios
from datetime import datetime
from Usuario import Usuario

def login()-> bool:
    lista_usuarios=get_usuarios()

    for i in range(3):
        nombre_usuario=input("Introduce tu nombre de usuario: ")
        existe_usuario = False

        for i,usuario_valido in enumerate(lista_usuarios):

            if nombre_usuario == usuario_valido.nombre:
                usuario = lista_usuarios[i]
                existe_usuario = True
                break
       
        if existe_usuario:
            contrasenha=input("Introduce tu contraseña: ")

            if contrasenha == usuario.contra:
                return True
            
            else:
                print(f"La contraseña es incorrecta\n")

        else:
            print(f"No existe ningun usuario llamado {nombre_usuario}\n")

    print("No has conseguido autenticarte, cerrando programa...")


def print_menu() -> None:
    lista_juegos=get_juegos()
    print("\nJUEGOS DISPONIBLES PARA COMPRAR:")
    for i,juego in enumerate(lista_juegos):
        print(f"[{i+1}]. {juego.nombre}")
    print("--------------------------------")

