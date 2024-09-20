import plotly.express as px

def curva_de_luz_reducida(nombre_cometa, curva_de_luz_procesada_df):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Apparent total magnitude processed', 'obs_method_key' : 'Observation Method'}
    fig = px.scatter(curva_de_luz_procesada_df, x='obs_date', y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title=f'Reduced Lightcurve of comet {nombre_cometa}')
    fig.update_yaxes(autorange="reversed")
    fig.show()
    print('✅ Curva de luz reducida creada.')