# Librerías
import requests

def conectar_con_API_de_COBS_Observaciones(nombre_cometa: str, conectado_a_internet: bool) -> object:
    '''
    Realiza la conexión con la API de COBS para generar la lista de observaciones. Retorna un objeto tipo Json.
    '''
    fecha_inicial = '1970-01-01 00:00'
    Link_cops_API = f'https://cobs.si/api/obs_list.api?des={nombre_cometa}&format=json&from_date={fecha_inicial}&exclude_faint=False&exclude_not_accurate=False'
   
    if conectado_a_internet:
        print(f'\n⌛ Conectando con la base de datos [COBS Observaciones].')
        response = requests.get(Link_cops_API)

        if response.status_code == 200:
            content = response.json()
            print('✅ Base de datos actualizada [COBS Observaciones].')
            return content

        else:
            print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response.status_code}\n{response.content}')

if __name__ == '__main__':
    conectar_con_API_de_COBS_Observaciones()
