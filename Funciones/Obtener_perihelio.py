# Librerías
import requests
import pandas as pd

# Conexión con la API de COBS para obtener el perihelio
def obtener_perihelio(nombre_cometa, conectado_a_internet):
    
    try: 
        Link_cops_API = f'https://cobs.si/api/comet.api?des={nombre_cometa}'

        if conectado_a_internet:
            print(f'⌛ Conectando con la base de datos [COBS].')
            response = requests.get(Link_cops_API)

            if response.status_code == 200:
                perihelio = pd.to_datetime(response.json()['object']['perihelion_date'])
                print('✅ Perihelio del cometa obtenido.')
                return perihelio
            
            else:
                print(f'🛑 El cometa: {nombre_cometa}, no se encuentra en la base de datos (COBS).')
                return None
        
    except requests.ConnectionError:
        print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response.status_code}\n{response.content}')

if __name__ == '__main__':
    obtener_perihelio()