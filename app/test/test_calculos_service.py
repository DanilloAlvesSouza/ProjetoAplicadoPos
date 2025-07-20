from app.services.calculos_service import taxa_para_pu
from decimal import Decimal

def test_taxa_para_pu_decimal():
    taxa = Decimal('10.0')
    prazo = 252  # 1 ano
    pu = taxa_para_pu(taxa, prazo)
    assert isinstance(pu, float)
    assert pu > 0

def test_taxa_para_pu_float():
    taxa = 10.0
    prazo = 252
    pu = taxa_para_pu(taxa, prazo)
    assert isinstance(pu, float)
    assert pu > 0

def test_taxa_para_pu_zero():
    taxa = 0.0
    prazo = 252
    pu = taxa_para_pu(taxa, prazo)
    assert isinstance(pu, float)
    assert pu > 0