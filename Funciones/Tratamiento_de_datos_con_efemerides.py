# Librerías
import numpy as np

def tratamiento_de_datos_con_efemerides(curva_de_luz_cruda_df, ephemeris, perihelio):
    
    # Creación del data frame ephemeris filtrada
    ephemeris_df = ephemeris.to_pandas()
    ephemeris_df.columns = ephemeris_df.columns.str.lower().str.replace(' ', '_')

    ephemeris_filtrada_df = ephemeris_df[['date', 'delta','r', 'phase']].copy()
    ephemeris_filtrada_df = ephemeris_filtrada_df.rename(columns = {'date':'obs_date'})

    # Unión de las bases de datos COBS y MPC
    curva_de_luz_procesada_df = curva_de_luz_cruda_df.merge(ephemeris_filtrada_df, on='obs_date')

    # Reducción de la magnitud aparente
    beta = 0

    curva_de_luz_procesada_df['magnitud_reducida'] = (
        curva_de_luz_cruda_df['magnitude'] 
        - 5 * np.log10(curva_de_luz_procesada_df['delta'] * curva_de_luz_procesada_df['r'])
        - (beta * curva_de_luz_procesada_df['phase'])
        )
    
    # Calculo del Delta t
    curva_de_luz_procesada_df['delta_t'] = (curva_de_luz_procesada_df.obs_date - perihelio) # type: ignore
    curva_de_luz_procesada_df['delta_t'] = curva_de_luz_procesada_df.delta_t.apply(lambda delta_t: delta_t.days)
    
    return curva_de_luz_procesada_df

if __name__ == '__main__':
    tratamiento_de_datos_con_efemerides()
