from Videojuego import Videojuego
from datos import get_juegos, get_usuarios
from datetime import datetime
from Usuario import Usuario

def print_menu() -> None:
    lista_juegos=get_juegos()
    print("JUEGOS DISPONIBLES PARA COMPRAR:")
    for i,juego in enumerate(lista_juegos):
        print(f"[{i+1}]. {juego.nombre}")
    print("--------------------------------")
print_menu()
