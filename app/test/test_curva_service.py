import os
import pytest
from app.services.curva_service import processar_futuros_di

@pytest.fixture
def insumos_exemplo():
    return [
        {
            "Ativo": {
                "Nome": "DI1",
                "Vencimento": "2025-07-20",
                "Atributos": {"Ultimo_Preco": 99.5}
            }
        },
        {
            "Ativo": {
                "Nome": "DI2",
                "Vencimento": "2025-08-20",
                "Atributos": {"Ultimo_Preco": 98.0}
            }
        }
    ]

def test_processar_futuros_di(monkeypatch, insumos_exemplo):
    # Garante que o cálculo de PU será feito
    monkeypatch.setenv("ConvertePUFator", "true")
    resultado = processar_futuros_di(insumos_exemplo)
    assert isinstance(resultado, list)
    assert len(resultado) > 0
    for ponto in resultado:
        assert "Vencimento" in ponto
        assert "PU" in ponto
        assert isinstance(ponto["PU"], float) or isinstance(ponto["PU"], int)