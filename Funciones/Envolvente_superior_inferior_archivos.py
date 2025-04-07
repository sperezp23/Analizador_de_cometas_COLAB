# Módulos 
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Conectar_con_API_de_MPC import conectar_con_API_de_MPC
from Funciones.Obtener_perihelio import obtener_perihelio
from Funciones.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Funciones.Promedio_movil_maximo import promedio_movil_maximo
from Funciones.Promedio_movil_minimo import promedio_movil_minimo

def envolvente_superior_inferior_archivos(nombre_cometa: str, curva_de_luz_cruda_df) -> tuple[object]:
    '''
    Procesa los datos del cometa especificado para calcular la 
    envolvente inferior de la curva de luz del cometa especificado.
    Retorna: 
    [1] curva_de_luz_cruda_df,
    [2] curva_de_luz_procesada_df, 
    [3] curva_de_luz_externa_df.
    [4] curva_de_luz_interna_df.
    ''' 

    if verificar_conexion():

        # Conexión con la API del MPC
        ephemeris = conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa)

        # Obtener perihelio de la API de COBS
        perihelio = obtener_perihelio(nombre_cometa, verificar_conexion())

        # Tratamiento de datos con efemerides
        curva_de_luz_procesada_df = tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, ephemeris, perihelio)

        # Promedio movil
        curva_de_luz_externa_df = promedio_movil_maximo(curva_de_luz_procesada_df)
        curva_de_luz_interna_df = promedio_movil_minimo(curva_de_luz_procesada_df)

        return curva_de_luz_cruda_df, curva_de_luz_procesada_df, curva_de_luz_externa_df, curva_de_luz_interna_df

if __name__ == '__main__':
    envolvente_superior_inferior_archivos()
