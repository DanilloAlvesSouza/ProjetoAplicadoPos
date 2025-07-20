from typing import Union
from decimal import Decimal, getcontext

def taxa_para_pu(taxa_percentual: Union[float, Decimal], prazo_dias) -> float:
    getcontext().prec = 10  
    prazo_anos = Decimal(prazo_dias) / Decimal(252)
    i = Decimal(taxa_percentual) / Decimal(100)
    constanteDaFormula = Decimal('1.0')
    pu = (constanteDaFormula / (constanteDaFormula + i) ** prazo_anos) * Decimal('10000')
    print(f"PU para taxa {taxa_percentual}% e prazo {prazo_anos} ano(s): {pu:.6f}")
    return float(pu)
