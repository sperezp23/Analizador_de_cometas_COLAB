# Librerías
import plotly.express as px

def crear_curvas_de_luz(variable,data_frame, titulo):

    labels = {
    'obs_date':'Observation Date',
    'obs_method_key' : 'Observation Method'
    }

    labels.update(variable)

    fig = px.scatter(data_frame, x='obs_date', y= list(variable.keys())[0], color='obs_method_key', template= 'plotly_dark', labels= labels, title= titulo)
    fig.update_yaxes(autorange="reversed")
    fig.show()

    if __name__ == '__main__':
        crear_curvas_de_luz()
