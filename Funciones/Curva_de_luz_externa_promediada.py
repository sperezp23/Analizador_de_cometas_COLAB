import plotly.express as px

def curva_de_luz_externa_promediada(nombre_cometa, curva_de_luz_externa_df):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Magnitude reduced'}
    fig = px.scatter(curva_de_luz_externa_df, x=curva_de_luz_externa_df.obs_date, y='promedio_movil', template= 'plotly_dark', labels= labels, title=f'Max Averaged Lightcurve of comet {nombre_cometa}')
    fig.update_traces(marker=dict(color='yellow', size=6, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_yaxes(autorange="reversed")
    fig.show()
    print('✅ Curva de luz promediada.')