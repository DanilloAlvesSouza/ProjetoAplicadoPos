from typing import Union
from decimal import Decimal,getcontext

def fator_juros_compostos(taxa, prazo):
    """
    Calcula o fator de desconto para juros compostos.
    
    :param taxa: taxa do período (exemplo: 0.05 para 5%)
    :param prazo: prazo em número de períodos (anos, meses, etc)
    :return: fator de desconto
    """
    return 1 / (1 + taxa) ** prazo

# Exemplo de uso:
taxa = 0.05  # 5%
prazo = 2    # 2 anos
fator = fator_juros_compostos(taxa, prazo)
print(f"Fator juros compostos: {fator:.6f}")


def taxa_para_pu(taxa_percentual: Union[float, Decimal], prazo_dias) -> float:
    getcontext().prec = 10  
    prazo_anos = Decimal(prazo_dias / 252)
    i = Decimal(taxa_percentual / 100  )
    constanteDaFormula = Decimal(1.0)
    pu = (constanteDaFormula / pow(constanteDaFormula + taxa_percentual, prazo_anos)) * 10000
    print(f"PU para taxa {taxa}% e prazo {prazo_anos} ano(s): {pu:.6f}")
    return pu
