from astroquery.mpc import MPC

def conectar_con_API_de_MPC(curva_de_luz_cruda_df, nombre_cometa):
    fecha_inicial = curva_de_luz_cruda_df.obs_date.min()
    fecha_final = curva_de_luz_cruda_df.obs_date.max()
    fechas = (fecha_final - fecha_inicial).days + 1 if (fecha_final - fecha_inicial).days + 1 <= 1441 else 1441

    ephemeris = MPC.get_ephemeris(nombre_cometa, start = str(fecha_inicial), number = fechas) # type: ignore  
    return ephemeris

if __name__ == '__main__':
    conectar_con_API_de_MPC()