import plotly.express as px

def curva_de_luz_externa(nombre_cometa, curva_de_luz_externa_df):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Max apparent total magnitude reduced', 'obs_method_key' : 'Observation Method'}
    fig = px.scatter(curva_de_luz_externa_df, x=curva_de_luz_externa_df.obs_date, y='magnitud_reducida', color='obs_method_key', template= 'plotly_dark', labels= labels, title=f'Max Lightcurve of comet {nombre_cometa}')
    fig.update_yaxes(autorange="reversed")
    fig.show()
    print('✅ Maxima curva de luz reducida creada.')