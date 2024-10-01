import os
from pathlib import Path
import plotly.express as px

def curva_de_luz_cruda(nombre_cometa,curva_de_luz_cruda_df):
    labels = {'obs_date':'Observation Date','magnitude':'Apparent total magnitude', 'obs_method_key' : 'Observation Method'}
    titulo = f'Crude lightcurve of {nombre_cometa}'

    carpeta_cometa = Path('Graficas', nombre_cometa.replace('/', '_'))

    if not os.path.exists('Graficas'):
        Path.mkdir('Graficas')
        
    ruta_archivos_graficas = f'{carpeta_cometa}/{titulo.replace('/', '_')}.png'
    
    if not os.path.exists(carpeta_cometa):
        Path.mkdir(carpeta_cometa)

    fig = px.scatter(curva_de_luz_cruda_df, x='obs_date', y='magnitude', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    fig.write_image(ruta_archivos_graficas)
    # fig.show()
    
    print('✅ Creada: curva de luz cruda creada.')

    if __name__ == '__main__':
        curva_de_luz_cruda()
