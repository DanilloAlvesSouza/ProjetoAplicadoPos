from app.curve_builder import build_risk_free_curve

def test_build_curve():
    insumos = [{
        "Ativo": {
            "Nome": "FUTURO_DI1Q25",
            "Vencimento": "2025-08-01",
            "Atributos": {
                "Ultimo_Preco": 14.91
            }
        }
    }]
    curva = build_risk_free_curve(insumos)
    assert isinstance(curva, list)
    assert "date" in curva[0] and "rate" in curva[0]
