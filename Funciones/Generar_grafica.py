# Funciones
from Funciones.Curva_de_luz_cruda import curva_de_luz_cruda
from Funciones.Curva_de_luz_reducida import curva_de_luz_reducida
from Funciones.Curva_de_luz_interna import curva_de_luz_interna
from Funciones.Curva_de_luz_interna_promediada import curva_de_luz_interna_promediada
from Funciones.Curva_de_luz_externa import curva_de_luz_externa
from Funciones.Curva_de_luz_externa_promediada import curva_de_luz_externa_promediada
from Funciones.Curvas_de_luz_interna_externa import curvas_de_luz_interna_externa

def generar_grafica(opcion_elegida: str,nombre_cometa: str, base_de_datos_1: object, base_de_datos_2: object = None) -> None:
    '''
    Genera la grafica especificada. Opciones a elegir:
    [1]: Curva de luz cruda,
    [2]: Curva de luz reducida,
    [3]: Curva de luz interna,
    [4]: Curva de luz interna promediada,
    [5]: Curva de luz externa,
    [6]: Curva de luz externa promediada,
    [7]: Curvas de luz  Interna y externa.
    '''
    if opcion_elegida == '1':
        curva_de_luz_cruda(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '2':
        curva_de_luz_reducida(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '3':
        curva_de_luz_interna(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '4':
        curva_de_luz_interna_promediada(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '5':
        curva_de_luz_externa(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '6':
        curva_de_luz_externa_promediada(nombre_cometa, base_de_datos_1)

    elif opcion_elegida == '7':
        curvas_de_luz_interna_externa(nombre_cometa, base_de_datos_1, base_de_datos_2)