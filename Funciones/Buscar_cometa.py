# Librerías
import pandas as pd

# Funciones
from Funciones.Conectar_con_API_de_COBS_Lista_de_Cometas import conectar_con_API_de_COBS_Lista_de_Cometas

def buscar_cometa(cometa_buscado, conectado_a_internet):
    cometas_hallados = []
    content = conectar_con_API_de_COBS_Lista_de_Cometas(conectado_a_internet)

    cometas_df = pd.DataFrame(content['objects'])
    lista_cometas_df = cometas_df[['name', 'fullname']]
    cometas_hallados =  lista_cometas_df.name[lista_cometas_df.fullname.str.contains(cometa_buscado)].values

    if len(cometas_hallados) == 0:
        print(f'🛑 No hay coincidencias para: {cometa_buscado}, en la base de datos (COBS).')
        return False
    
    else:
        print(f'✅ Coincidencias halladas:\n{cometas_hallados}')
        return True

if __name__ == '__main__':
    buscar_cometa()