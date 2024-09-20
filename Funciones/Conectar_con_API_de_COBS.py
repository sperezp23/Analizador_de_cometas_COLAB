import requests

def conectar_con_API_de_COBS(conectado_a_internet):
    nombre_cometa = input('Ingrese el nombre del cometa:\n') #'C/2023 A3' 

    Link_cops_API = f'https://cobs.si/api/obs_list.api?des={nombre_cometa}&format=json&from_date=&to_date=&exclude_faint=False&exclude_not_accurate=False'

    if conectado_a_internet:
        response = requests.get(Link_cops_API)

        if response.status_code == 200:
            content = response.json()
            print('✅ Base de datos actualizada.')
            return nombre_cometa, content

        else:
            print(f'🛑 Se presentó un error al cargar la base de datos.\nError: {response.status_code}\n{response.content}')

if __name__ == '__main__':
    conectar_con_API_de_COBS()