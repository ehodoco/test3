from Videojuego import Videojuego
from datos import get_juegos, get_usuarios
from datetime import datetime
from Usuario import Usuario

def comprobar_usuario(nombre_usuario:str, lista_usuarios:list[object]) -> object :
    for i,usuario_valido in enumerate(lista_usuarios):

        if nombre_usuario == usuario_valido.nombre:
            usuario = lista_usuarios[i]
            return usuario


def comprobar_contrasenha(intento_contrasenha:str, usuario:object) -> bool:
    if intento_contrasenha == usuario.contra:
        return True
    
    else:
        return False


def login() -> object:
    lista_usuarios = get_usuarios()
    intentos = 0
    existe_usuario = False
    contrasenha_correcta = False

    usuario=comprobar_usuario(input("Login: "), lista_usuarios)

    while intentos < 2 and usuario == None:
        intentos += 1
        print("El nombre de usuario no existe")
        usuario=comprobar_usuario(input("Inserte de nuevo el nombre: "), lista_usuarios)

    if usuario != None:
        existe_usuario = True

    if existe_usuario:
        contrasenha_correcta = comprobar_contrasenha(input("Inserte la contraseña: "), usuario)

        while intentos < 2 and contrasenha_correcta == False:
            intentos += 1
            contrasenha_correcta = comprobar_contrasenha(input("Contraseña incorrecta, inserte de nuevo la contraseña: "), usuario)
    
    if contrasenha_correcta:
        return usuario

    if intentos >= 2:
        print("No has conseguido identificarte, cerrando programa...")
        return None


def juegos_aptos(usuario:object) -> list[object]:
    lista_juegos=get_juegos()
    edad_usuario = usuario.edad()
    lista_juegos_aptos = []

    for juego in lista_juegos:
        if edad_usuario >= juego.PEGI:
            lista_juegos_aptos.append(juego)

    return lista_juegos_aptos


def print_menu(lista_juegos:list[object]) -> None:
    print("JUEGOS DISPONIBLES PARA COMPRAR:")

    for i,juego in enumerate(lista_juegos):
        print(f"[{i+1}]. {juego.nombre}, precio: {juego.precio_final(0, 0)}")
    print("-------------------------------- \n")


def ingresar_dinero() -> float:
    while True:
        try:
            dinero = float(input("Cantidad a ingresar: "))
        except:
            print("Cantidad de dinero no válida, intentelo de nuevo")
        else:
            decimales_dinero_sobre2 = 100*(100*dinero-int(100*dinero))

            if dinero < 0 or decimales_dinero_sobre2 != 0.0:
                print("Cantidad de dinero no válida, intentelo de nuevo")
            else:
                return dinero


def print_lista_juegos(lista_juegos:list[object]) -> None:
    for juego in lista_juegos:
            print(juego.nombre)


def precio_carrito(carrito:list[object]) -> float:
    precio_total = 0

    for juego in carrito:
        precio_juego = juego.precio_final(0, 0)
        print(f"{juego.nombre} -- precio: {precio_juego}€")
        precio_total += precio_juego

    print(f"El precio total es {precio_total}")

    return precio_total

