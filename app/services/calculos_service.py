from typing import Union
from decimal import Decimal,getcontext

def taxa_para_pu(taxa_percentual: Union[float, Decimal], prazo_dias) -> float:
    getcontext().prec = 10  
    prazo_anos = Decimal(prazo_dias / 252)
    i = Decimal(taxa_percentual / 100  )
    constanteDaFormula = Decimal(1.0)
    pu = (constanteDaFormula / pow(constanteDaFormula + taxa_percentual, prazo_anos)) * 10000
    print(f"PU para taxa {taxa_percentual}% e prazo {prazo_anos} ano(s): {pu:.6f}")
    return pu
