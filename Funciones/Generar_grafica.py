# Funciones
from Funciones.Crear_curvas_de_luz import crear_curvas_de_luz
from Funciones.Curvas_de_luz_interna_externa import curvas_de_luz_interna_externa

def generar_grafica(opcion_elegida: str, nombre_cometa: str, bases_de_datos: tuple[object]) -> None:
    '''
    Genera la grafica especificada. Opciones a elegir:
    [1]: Curva de luz cruda,
    [2]: Curva de luz reducida,
    [3]: Curva de luz externa,
    [4]: Curva de luz externa promediada,
    [5]: Curva de luz interna,
    [6]: Curva de luz interna promediada,
    [7]: Curvas de luz  interna y externa.
    '''

    if opcion_elegida == '1':

        variable_a_graficar  = {'magnitude': 'Crude magnitude'}
        titulo = f'Crude lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[0], titulo)

    elif opcion_elegida == '2':

        variable_a_graficar  = {'magnitud_reducida' :'Reduced magnitude'}
        titulo = f'Reduced lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[1], titulo)

    elif opcion_elegida == '3':

        variable_a_graficar  = {'magnitud_reducida':'Maximized reduced magnitude'}
        titulo = f'Maximized external lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[2], titulo)

    elif opcion_elegida == '4':

        variable_a_graficar = {'promedio_movil':'Averaged reduced magnitude'}
        titulo = f'Averaged external lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[2], titulo, promediada = True, color = 'yellow')

    elif opcion_elegida == '5':

        variable_a_graficar  = {'magnitud_reducida':'Minimized reduced magnitude'}
        titulo = f'Minimized external lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[3], titulo)

    elif opcion_elegida == '6':
        variable_a_graficar = {'promedio_movil':'Averaged reduced magnitude'}
        titulo = f'Averaged internal lightcurve of {nombre_cometa}'

        crear_curvas_de_luz(variable_a_graficar , bases_de_datos[3], titulo, promediada = True, color = 'red')

    elif opcion_elegida == '7':
        
        curvas_de_luz_interna_externa(nombre_cometa, bases_de_datos[2],bases_de_datos[3])