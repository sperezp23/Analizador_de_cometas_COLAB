import plotly.express as px

def grafica_de_luz_cruda(nombre_cometa,curva_de_luz_cruda_df):
    labels = {'obs_date':'Observation Date','magnitude':'Apparent total magnitude', 'obs_method_key' : 'Observation Method'}
    fig = px.scatter(curva_de_luz_cruda_df, x='obs_date', y='magnitude', color='obs_method_key', template= 'plotly_dark', labels= labels, title=f'Lightcurve of {nombre_cometa}')
    fig.update_yaxes(autorange="reversed")
    fig.show()
    print('✅ Curva de luz cruda creada.')