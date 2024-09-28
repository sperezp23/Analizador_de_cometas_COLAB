# %% Funciones  
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Buscar_cometa import buscar_cometa
from Funciones.Envolvente import envolvente
from Funciones.Verificar_cometa import verificar_cometa

# %% Variables
Terminar = False
opcion_elegida = '-1'
opciones = '123'
texto_opciones = f'''{'-'*40}\nElija una de las siguientes opciones:
[1] : Buscar un comenta.
[2] : Graficar curvas de luz.
[3] : Finalizar programa.\n'''

# %% Verificar la conexión a internet.
conectado_a_internet = verificar_conexion()

# %% Ciclo principal
while (conectado_a_internet) and ( not(Terminar)):

    # Leer opcion elegida
    while True:
        if opcion_elegida in opciones:
            break
        else:
            opcion_elegida = input(texto_opciones)

    # Buscar cometa
    if opcion_elegida == '1':
        cometa_buscado = input('\nIngrese el nombre del cometa que desea buscar:\n')
        buscar_cometa(cometa_buscado, conectado_a_internet)
    
    # Graficar curvas de luz 
    elif opcion_elegida == '2':
        nombre_cometa = input('\nIngrese el nombre del cometa:\n') #'C/2023 A3'

        if verificar_cometa(nombre_cometa, conectado_a_internet):
            envolvente(nombre_cometa, conectado_a_internet)

    # Finalizar programa
    elif opcion_elegida == '3':
        break

    # Resetear opción elegida
    opcion_elegida = '-1'

    # Verificar la conexión a internet.
    conectado_a_internet = verificar_conexion()