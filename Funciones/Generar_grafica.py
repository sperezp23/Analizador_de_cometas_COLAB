# Funciones
from Funciones.Curva_de_luz_cruda import curva_de_luz_cruda
from Funciones.Curva_de_luz_reducida import curva_de_luz_reducida
from Funciones.Curva_de_luz_interna import curva_de_luz_interna
from Funciones.Curva_de_luz_interna_promediada import curva_de_luz_interna_promediada

def generar_grafica(opcion_elegida,nombre_cometa, base_de_datos):
    if opcion_elegida == '1':
        curva_de_luz_cruda(nombre_cometa, base_de_datos)

    elif opcion_elegida == '2':
        curva_de_luz_reducida(nombre_cometa, base_de_datos)

    elif opcion_elegida == '3':
        curva_de_luz_interna(nombre_cometa, base_de_datos)

    elif opcion_elegida == '4':
        curva_de_luz_interna_promediada(nombre_cometa, base_de_datos)