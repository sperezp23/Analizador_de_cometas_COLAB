# Librerías
import plotly.express as px

# Funciones
# from Funciones.Crear_carpetas import crear_carpetas

def curva_de_luz_cruda(nombre_cometa,curva_de_luz_cruda_df):
    labels = {'obs_date':'Observation Date',
              'magnitude':'Apparent total magnitude crude',
              'obs_method_key' : 'Observation Method'
              }
    
    titulo = f'Crude lightcurve of {nombre_cometa}'

    # ruta_archivos_graficas = crear_carpetas(nombre_cometa, titulo)

    fig = px.scatter(curva_de_luz_cruda_df, x='obs_date', y='magnitude', color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    # fig.write_image(ruta_archivos_graficas)
    fig.show()

    if __name__ == '__main__':
        curva_de_luz_cruda()
