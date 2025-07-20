import numpy as np
from scipy.interpolate import interp1d
from decimal import Decimal
from datetime import timedelta
import os

def interporlador_pu(curva_prazos):
    """
    Recebe uma lista de dicionários com as chaves 'DU', 'PU' e 'Vencimento' (data) e retorna uma nova lista
    preenchendo os PUs interpolados para todos os prazos inteiros entre o menor e o maior DU, incluindo a data de prazo.
    """
    if len(curva_prazos) < 2:
        raise ValueError("É necessário pelo menos dois pontos para interpolação.")

    prazos = [r['DU'] for r in curva_prazos]
    pu = [float(r['PU']) for r in curva_prazos]
    datas = {r['DU']: r['Vencimento'] for r in curva_prazos}  # Mapeia DU para data

    if os.environ.get("METODO_INTERPORLACAO") == "EXPONENCIAL":
        pu = np.log(pu)
    
    interpolador_log = interp1d(prazos, pu, kind='linear', fill_value="extrapolate")

    menor_prazo = int(min(prazos))
    maior_prazo = int(max(prazos))
    prazos_interpolados = list(range(menor_prazo, maior_prazo + 1))

    curva_interpolada = []
    data_anterior = None
    for du in prazos_interpolados:
        pu_interp = float(interpolador_log(du))
        if os.environ.get("METODO_INTERPORLACAO") == "EXPONENCIAL":
            pu_interp = float(np.exp(pu_interp))
        
        data_venc = datas.get(du, None)
        if data_venc is None:
            if data_anterior is not None:
                data_venc = data_anterior + timedelta(days=1)
            else:
                data_venc = None
        curva_interpolada.append({'DC': du, 'PU': pu_interp, 'Vencimento': data_venc})
        data_anterior = data_venc

    return curva_interpolada