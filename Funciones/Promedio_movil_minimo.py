def promedio_movil_minimo(curva_de_luz_procesada_df, numero_elementos_grupo = 9):
    curva_de_luz_externa_df = curva_de_luz_procesada_df.groupby(by = 'obs_date').max()
    curva_de_luz_externa_df = curva_de_luz_externa_df.reset_index()

    curva_de_luz_externa_df = curva_de_luz_externa_df.copy()
    curva_de_luz_externa_df['promedio_movil'] = curva_de_luz_externa_df.magnitud_reducida.rolling(window = numero_elementos_grupo, center= True).mean()

    return curva_de_luz_externa_df

if __name__ == '__main__':
    promedio_movil_minimo()