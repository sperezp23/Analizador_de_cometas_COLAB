# %% Librerías
import requests
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from astroquery.mpc import MPC

# %% Funciones  
from Verificar_conexion import verificar_conexion
from Conectar_con_API_de_COBS import conectar_con_API_de_COBS
from Tratamiento_de_datos_cometa import tratamiento_de_datos_cometa
from Grafica_de_luz_cruda import grafica_de_luz_cruda
from Conectar_con_API_de_MPC import conectar_con_API_de_MPC 

# Verificar la conexión a internet.
verificar_conexion()

# %%  Conexión con la API de COBS
nombre_cometa, content = conectar_con_API_de_COBS()

# %% Tratamiento de datos
curva_de_luz_cruda_df = tratamiento_de_datos_cometa(content)

# %%  Curva de luz cruda.
grafica_de_luz_cruda(nombre_cometa, curva_de_luz_cruda_df)

# %%  Creación de data frame Ephemeris (conexión con la API del MPC)
ephemeris_df = conectar_con_API_de_MPC(curva_de_luz_cruda_df)
# %% Creación del data frame ephemeris filtrada
ephemeris_filtrada_df = ephemeris_df[['date', 'delta','r', 'phase']].copy()
ephemeris_filtrada_df = ephemeris_filtrada_df.rename(columns = {'date':'obs_date'})

# %% Unión de las bases de datos COBS y MPC
curva_de_luz_procesada_df = curva_de_luz_cruda_df.merge(ephemeris_filtrada_df, on='obs_date')

# Reducción de la magnitud aparente
beta = 0

curva_de_luz_procesada_df['magnitud_reducida'] = (
    curva_de_luz_cruda_df['magnitude'] 
    - 5 * np.log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
    - (beta * curva_de_luz_procesada_df['phase'])
    )

# %% Curva de luz reducida
labels = {'obs_date':'Observation Date','magnitud_reducida':'Apparent total magnitude processed', 'obs_method_key' : 'Observation Method'}
fig = px.scatter(curva_de_luz_procesada_df, x='obs_date', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title=f'Reduced Lightcurve of comet {nombre_cometa}')
fig.update_yaxes(autorange="reversed")
fig.show()
print('✅ Curva de luz reducida creada.')

# %% Creación del data frame curva de luz agrupada
curva_de_luz_externa_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').min()
curva_de_luz_externa_df = curva_de_luz_externa_df.reset_index()

# %%  Creación del data frame curva de luz promediada
numero_elementos_grupo = 7

curva_de_luz_externa_df = curva_de_luz_externa_df.copy()
curva_de_luz_externa_df['promedio_movil'] = curva_de_luz_externa_df.magnitud_reducida.rolling(window = numero_elementos_grupo).mean()

# %% Curva de luz reducida
labels = {'obs_date':'Observation Date','magnitud_reducida':'Max apparent total magnitude reduced', 'obs_method_key' : 'Observation Method'}
fig = px.scatter(curva_de_luz_externa_df, x=curva_de_luz_externa_df.obs_date, y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title=f'Max Lightcurve of comet {nombre_cometa}')
fig.update_yaxes(autorange="reversed")
fig.show()
print('✅ Maxima curva de luz reducida creada.')

# %%  Gráfica de luz promediada
labels = {'obs_date':'Observation Date','magnitud_reducida':'Magnitude reduced'}
fig = px.scatter(curva_de_luz_externa_df, x=curva_de_luz_externa_df.obs_date, y='promedio_movil', template= 'plotly_dark', labels= labels, title=f'Max Averaged Lightcurve of comet {nombre_cometa}')
fig.update_traces(marker=dict(color='yellow', size=6, line=dict(width=1, color='DarkSlateGrey')))
fig.update_yaxes(autorange="reversed")
fig.show()
print('✅ Curva de luz promediada.')