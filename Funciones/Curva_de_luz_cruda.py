import plotly.express as px

def curva_de_luz_cruda(nombre_cometa,curva_de_luz_cruda_df):
    labels = {'obs_date':'Observation Date','magnitude':'Apparent total magnitude', 'obs_method_key' : 'Observation Method'}
    titulo = f'Crude lightcurve of {nombre_cometa}'
    fig = px.scatter(curva_de_luz_cruda_df, x='obs_date', y='magnitude', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    # fig.write_image(f'Graficas\\{r'' + titulo}.png')
    fig.show()
    print('✅ Curva de luz cruda creada.')

    if __name__ == '__main__':
        curva_de_luz_cruda()
