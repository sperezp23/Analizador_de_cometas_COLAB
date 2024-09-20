def conectar_con_API_de_MPC(curva_de_luz_cruda_df):
    fecha_inicial = curva_de_luz_cruda_df.obs_date.min()
    fecha_final = curva_de_luz_cruda_df.obs_date.max()
    fechas = (fecha_final - fecha_inicial).days + 1 if (fecha_final - fecha_inicial).days <= 1441 else 1441

    ephemeris = MPC.get_ephemeris(nombre_cometa, start = str(fecha_inicial), number = fechas) # type: ignore

    ephemeris_df = ephemeris.to_pandas()
    ephemeris_df.columns = ephemeris_df.columns.str.lower().str.replace(' ', '_')
    return ephemeris_df