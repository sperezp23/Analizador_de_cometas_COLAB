import requests
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from astroquery.mpc import MPC

def verificar_conexion():
    try:
        requests.get("http://www.google.com", timeout=5)
        print('✅ Conectado a internet.')
        print('✅ Conectando con la base de datos.')
        return True
    
    except requests.ConnectionError:
        print('🛑 Sin conexión a internet.')
        return False
    