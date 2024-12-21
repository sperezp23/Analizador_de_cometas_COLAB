import pandas as pd
from astroquery.mpc import MPC

def conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa):
    fecha_inicial = curva_de_luz_cruda_df.obs_date.min()
    fecha_final = curva_de_luz_cruda_df.obs_date.max()
    fechas = (fecha_final - fecha_inicial).days + 1 if (fecha_final - fecha_inicial).days + 1 <= 1441 else 1441

    print('⌛ Conectando con la base de datos [MPC efemerides].')
    ephemeris = MPC.get_ephemeris(nombre_cometa, start = str(fecha_inicial), number = fechas)

    # Creación del data frame ephemeris filtrada
    ephemeris_df = ephemeris.to_pandas()
    ephemeris_df.columns = ephemeris_df.columns.str.lower().str.replace(' ', '_')

    ephemeris_filtrada_df = ephemeris_df[['date', 'delta','r', 'phase']].copy()
    ephemeris_filtrada_df = ephemeris_filtrada_df.rename(columns = {'date':'obs_date'})
    ephemeris_filtrada_df['obs_date'] = pd.to_datetime(pd.to_datetime(ephemeris_filtrada_df.obs_date).dt.date)

    print('✅ Base de datos actualizada [MPC efemerides].')
    return ephemeris_filtrada_df

if __name__ == '__main__':
    conectar_con_API_de_MPC()