# Librerías
import os
from pathlib import Path
from datetime import date

def crear_carpetas(nombre_cometa, titulo, tipo_de_grafica):
    fecha_actual = str(date.today())
    carpeta_cometa = Path('Graficas', nombre_cometa.replace('/', '_'))
    carpeta_tipo_de_grafica = Path(carpeta_cometa, tipo_de_grafica)
    carpeta_fecha = Path(carpeta_tipo_de_grafica, fecha_actual)

    if not os.path.exists('Graficas'):
        Path.mkdir('Graficas')

    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    if not os.path.exists(carpeta_tipo_de_grafica):
        Path.mkdir(carpeta_tipo_de_grafica)

    if not os.path.exists(carpeta_fecha):
        Path.mkdir(carpeta_fecha)

    return f'{carpeta_fecha}/{titulo.replace('/', '_')}__{fecha_actual}.png'

if __name__ == '__main__':
    crear_carpetas()
