import requests

def verificar_conexion():
    try:
        requests.get("http://www.google.com", timeout=5)
        print('✅ Conectado a internet.')
        print('✅ Conectando con la base de datos.')
        return True
    
    except requests.ConnectionError:
        print('🛑 Sin conexión a internet.')
        return False

if __name__ == '__main__':
    verificar_conexion()