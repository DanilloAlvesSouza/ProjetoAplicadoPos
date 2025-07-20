import numpy as np
from scipy.interpolate import interp1d
from decimal import Decimal
from datetime import timedelta

def interporlador_pu(curva_prazos):
    """
    Recebe uma lista de dicionários com as chaves 'DU', 'PU' e 'Vencimento' (data) e retorna uma nova lista
    preenchendo os PUs interpolados para todos os prazos inteiros entre o menor e o maior DU, incluindo a data de prazo.
    """
    if len(curva_prazos) < 2:
        raise ValueError("É necessário pelo menos dois pontos para interpolação.")

    prazos = [r['DU'] for r in curva_prazos]
    pus = [float(r['PU']) for r in curva_prazos]
    datas = {r['DU']: r['Vencimento'] for r in curva_prazos}  # Mapeia DU para data

    pu_log = np.log(pus)
    interpolador_log = interp1d(prazos, pu_log, kind='linear', fill_value="extrapolate")

    menor_prazo = int(min(prazos))
    maior_prazo = int(max(prazos))
    prazos_interpolados = list(range(menor_prazo, maior_prazo + 1))

    curva_interpolada = []
    data_anterior = None
    for du in prazos_interpolados:
        log_pu_interp = interpolador_log(du)
        pu_interp = float(np.exp(log_pu_interp))
        data_venc = datas.get(du, None)
        if data_venc is None:
            if data_anterior is not None:
                data_venc = data_anterior + timedelta(days=1)
            else:
                data_venc = None
        curva_interpolada.append({'DC': du, 'PU': pu_interp, 'Vencimento': data_venc})
        data_anterior = data_venc

    return curva_interpolada

# # Exemplo de uso:
# curvaPrazos = [
#     {'DU': 100, 'PU': 10, 'Vencimento': '2023-01-01'},
#     {'DU': 200, 'PU': 20, 'Vencimento': '2023-02-01'},
#     {'DU': 300, 'PU': 30, 'Vencimento': '2023-03-01'},
# ]

# curva_interpolada = interpolar_pu(curvaPrazos)
# for ponto in curva_interpolada:
#     print(f"DU={ponto['DU']}, PU={ponto['PU']:.6f}, Vencimento={ponto['Vencimento']}")
