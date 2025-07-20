import os
import numpy as np
from datetime import date
from app.services.interpolador import interporlador_pu

def test_interporlador_pu_linear():
    curva_prazos = [
        {'DU': 0, 'PU': 100.0, 'Vencimento': date(2025, 7, 20)},
        {'DU': 2, 'PU': 110.0, 'Vencimento': date(2025, 7, 22)},
    ]
    os.environ["METODO_INTERPORLACAO"] = "LINEAR"
    resultado = interporlador_pu(curva_prazos)
    assert isinstance(resultado, list)
    assert len(resultado) == 3  # DU 0, 1, 2
    assert resultado[0]['PU'] == 100.0
    assert resultado[-1]['PU'] == 110.0
    # O valor intermediário deve ser a média aritmética
    assert np.isclose(resultado[1]['PU'], 105.0)

def test_interporlador_pu_exponencial():
    curva_prazos = [
        {'DU': 0, 'PU': 100.0, 'Vencimento': date(2025, 7, 20)},
        {'DU': 2, 'PU': 200.0, 'Vencimento': date(2025, 7, 22)},
    ]
    os.environ["METODO_INTERPORLACAO"] = "EXPONENCIAL"
    resultado = interporlador_pu(curva_prazos)
    assert isinstance(resultado, list)
    assert len(resultado) == 3  # DU 0, 1, 2
    assert np.isclose(resultado[0]['PU'], 100.0)
    assert np.isclose(resultado[-1]['PU'], 200.0)
    # O valor intermediário deve ser a média geométrica
    assert np.isclose(resultado[1]['PU'], np.sqrt(100.0 * 200.0))