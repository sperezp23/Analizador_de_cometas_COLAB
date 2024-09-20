# %% Funciones  
from Funciones.Verificar_conexion import verificar_conexion
from Funciones.Conectar_con_API_de_COBS import conectar_con_API_de_COBS
from Funciones.Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Funciones.Curva_de_luz_cruda import curva_de_luz_cruda
from Funciones.Conectar_con_API_de_MPC import conectar_con_API_de_MPC
from Funciones.Tratamiento_de_datos_con_efemerides import tratamiento_de_datos_con_efemerides
from Funciones.Curva_de_luz_reducida import curva_de_luz_reducida
from Funciones.Promedio_movil import promedio_movil
from Funciones.Curva_de_luz_externa import curva_de_luz_externa
from Funciones.Curva_de_luz_externa_promediada import curva_de_luz_externa_promediada

# Verificar la conexión a internet.
conectado_a_internet = verificar_conexion()

# %%  Conexión con la API de COBS
nombre_cometa, content = conectar_con_API_de_COBS(conectado_a_internet)

# %% Tratamiento de datos
curva_de_luz_cruda_df = tratamiento_de_datos_cometa(content)

# %%  Curva de luz cruda.
curva_de_luz_cruda(nombre_cometa, curva_de_luz_cruda_df)

# %%  Conexión con la API del MPC
ephemeris = conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa)

# %% Tratamiento de datos
curva_de_luz_procesada_df = tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, ephemeris)

# %% Curva de luz reducida
curva_de_luz_reducida(nombre_cometa, curva_de_luz_procesada_df)

# %% Creación del data frame curva de luz agrupada
curva_de_luz_externa_df = promedio_movil(curva_de_luz_procesada_df)

# %% Curva de luz reducida
curva_de_luz_externa(nombre_cometa, curva_de_luz_externa_df)

# %%  Gráfica de luz promediada
curva_de_luz_externa_promediada(nombre_cometa, curva_de_luz_externa_df)