# Librerías
import plotly.express as px

def curva_de_luz_interna_promediada(nombre_cometa, curva_de_luz_interna_df):
    labels = {
        'obs_date':'Observation Date',
        'promedio_movil':'Averaged reduced magnitude'
        }
    
    titulo = f'Averaged internal lightcurve of {nombre_cometa}'

    fig = px.scatter(curva_de_luz_interna_df, x='obs_date', y='promedio_movil', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_traces(marker=dict(color='red', size=6, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_yaxes(autorange="reversed")
    fig.show()

if __name__ == '__main__':
    curva_de_luz_interna_promediada()
