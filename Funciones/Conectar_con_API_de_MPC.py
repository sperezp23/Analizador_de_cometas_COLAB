import pandas as pd
from math import ceil
from astroquery.mpc import MPC

def conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa):
    ephemeris_total = []

    fecha_inicial = curva_de_luz_cruda_df.obs_date.min()
    fecha_final = curva_de_luz_cruda_df.obs_date.max()
    fechas = (fecha_final - fecha_inicial).days + 1

    print('⌛ Conectando con la base de datos [MPC efemerides].')
    for i in range(ceil(fechas/1441)):
        ephemeris = MPC.get_ephemeris(nombre_cometa, start = str(fecha_inicial), number = 1441)
        ephemeris_ciclo_df = ephemeris.to_pandas()
        ephemeris_total.append(ephemeris_ciclo_df)
    
        fecha_inicial = ephemeris_ciclo_df.Date.max()

    # Creación del data frame ephemeris filtrada
    ephemeris_df = pd.concat(ephemeris_total)
    ephemeris_df.columns = ephemeris_df.columns.str.lower().str.replace(' ', '_')

    ephemeris_filtrada_df = ephemeris_df[['date', 'delta','r', 'phase']].copy()
    ephemeris_filtrada_df = ephemeris_filtrada_df.rename(columns = {'date':'obs_date'})
    ephemeris_filtrada_df['obs_date'] = pd.to_datetime(pd.to_datetime(ephemeris_filtrada_df.obs_date).dt.date)
    ephemeris_filtrada_df.reset_index(inplace = True)

    print('✅ Base de datos actualizada [MPC efemerides].')
    return ephemeris_filtrada_df

if __name__ == '__main__':
    conectar_con_API_de_MPC()