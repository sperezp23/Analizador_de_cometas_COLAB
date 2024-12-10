# Funciones  
from Funciones.Conectar_con_API_de_COBS_Observaciones import conectar_con_API_de_COBS_Observaciones
from Funciones.Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Funciones.Conectar_con_API_de_MPC import conectar_con_API_de_MPC
from Funciones.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Funciones.Promedio_movil_maximo import promedio_movil_maximo

def envolvente_superior(nombre_cometa, conectado_a_internet):
    # Conexión con la API de COBS
    content = conectar_con_API_de_COBS_Observaciones(nombre_cometa, conectado_a_internet)

    # Tratamiento de datos observacionales
    curva_de_luz_cruda_df = tratamiento_de_datos_cometa(content)

    # Conexión con la API del MPC
    ephemeris = conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa)

    # Tratamiento de datos con efemerides
    curva_de_luz_procesada_df = tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, ephemeris)

    # Promedio movil
    curva_de_luz_externa_df = promedio_movil_maximo(curva_de_luz_procesada_df)

    return curva_de_luz_cruda_df, curva_de_luz_procesada_df, curva_de_luz_externa_df

if __name__ == '__main__':
    envolvente_superior()
