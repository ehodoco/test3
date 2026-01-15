from datetime import datetime


class Usuario:
    def __init__(self, nombre: str, contra: str, fecha_nac: datetime, saldo: float):
        self.nombre = nombre
        self.contra = contra
        self.fecha_nac = fecha_nac
        self.saldo = round(saldo, 2)

    def edad(self) -> int:
        hoy = datetime.now()
        return hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))

