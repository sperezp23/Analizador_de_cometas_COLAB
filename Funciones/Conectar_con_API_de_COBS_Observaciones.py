# Librerías
import requests

# Funciones
from Funciones.Buscar_cometa import buscar_cometa

def conectar_con_API_de_COBS_Observaciones(nombre_cometa, conectado_a_internet):   
    Link_cops_API = f'https://cobs.si/api/obs_list.api?des={nombre_cometa}&format=json&from_date=&to_date=&exclude_faint=False&exclude_not_accurate=False'

    if conectado_a_internet:
        print(f'{'-'*40}\n✅ Conectando con la base de datos.')
        response = requests.get(Link_cops_API)

        if response.status_code == 200:
            content = response.json()
            print('✅ Base de datos actualizada [COBS Observaciones].')
            return content

        else:
            print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response.status_code}\n{response.content}')

if __name__ == '__main__':
    conectar_con_API_de_COBS_Observaciones()