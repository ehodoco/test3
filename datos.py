from Videojuego import Videojuego
from Usuario import Usuario
from datetime import datetime

def get_juegos() -> list:
    return [
        Videojuego("Zelda: Breath of the Wild", ["Aventura", "Acción"], datetime(2017, 3, 3), 97, 12, 59.99, 14.4),
        Videojuego("Grand Theft Auto V", ["Acción", "Mundo Abierto"], datetime(2013, 9, 17), 96, 18, 39.99, 72),
        Videojuego("Resident Evil 2 Remake", ["Terror", "Supervivencia"], datetime(2019, 1, 25), 91, 18, 29.99, 26),
        Videojuego("The Last of Us Part II", ["Acción", "Aventura", "Terror"], datetime(2020, 6, 19), 93, 18, 49.99, 78),
        Videojuego("Dark Souls III", ["RPG", "Acción"], datetime(2016, 4, 12), 89, 16, 49.99, 25),
        Videojuego("Red Dead Redemption 2", ["Aventura", "Mundo Abierto"], datetime(2018, 10, 26), 96, 18, 59.99, 150),
        Videojuego("Minecraft", ["Sandbox", "Supervivencia"], datetime(2011, 8, 11), 93, 7, 23.99, 1),
        Videojuego("Hollow Knight", ["Metroidvania", "Plataformas"], datetime(2017, 2, 24), 90, 7, 14.99, 3),
        Videojuego("DOOM Eternal", ["FPS", "Acción"], datetime(2020, 3, 20), 88, 18, 39.99, 50),
        Videojuego("Cyberpunk 2077", ["RPG", "Mundo Abierto"], datetime(2020, 12, 10), 86, 18, 59.99, 70),
        Videojuego("Stardew Valley", ["Simulación", "RPG"], datetime(2016, 2, 26), 89, 3, 13.99, 0.5),
        Videojuego("Bloodborne", ["RPG", "Acción", "Terror"], datetime(2015, 3, 24), 92, 16, 39.99, 25)
    ]


def get_usuarios() -> list:
    return [
        Usuario("Paco", "abc", datetime(1987, 3, 5), 0),
        Usuario("Paquirrin", "123", datetime(2010, 4, 4), 75.35)
    ]


