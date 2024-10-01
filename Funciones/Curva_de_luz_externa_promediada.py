import os
from pathlib import Path
import plotly.express as px

def curva_de_luz_externa_promediada(nombre_cometa, curva_de_luz_externa_df):
    labels = {'obs_date':'Observation Date','magnitud_reducida':'Magnitude reduced'}
    titulo = f'Averaged external lightcurve of {nombre_cometa}'

    carpeta_cometa = Path('Graficas', nombre_cometa.replace('/', '_'))

    if not os.path.exists('Graficas'):
        Path.mkdir('Graficas')

    ruta_archivos_graficas = f'{carpeta_cometa}/{titulo.replace('/', '_')}.png'

    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    fig = px.scatter(curva_de_luz_externa_df, x=curva_de_luz_externa_df.obs_date, y='promedio_movil', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_traces(marker=dict(color='yellow', size=6, line=dict(width=1, color='DarkSlateGrey')))
    fig.update_yaxes(autorange="reversed")
    fig.write_image(ruta_archivos_graficas)
    # fig.show()
    
    print('✅ Creada: curva de luz promediada.')

if __name__ == '__main__':
    curva_de_luz_externa_promediada()