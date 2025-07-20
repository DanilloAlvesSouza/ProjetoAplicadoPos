from models.ativo import Ativo
from datetime import datetime
from decimal import Decimal
from Utils.utils import ContaDiaUtil
from services.calculos_service import taxa_para_pu
from services.interpolador import interporlador_pu

def montaAtivosD1(insumos):
    ativos = []

    for item in insumos:
        ativo_dict = item['Ativo']
        nome = ativo_dict['Nome']
        vencimento = ativo_dict['Vencimento']
        atributos = ativo_dict['Atributos']
        
        ativo = Ativo(
            nome=nome,
            vencimento=vencimento,
            ultimo_preco= str(atributos['Ultimo_Preco'])
        )

        ativos.append(ativo)

    # Retorna lista de objetos ou realiza processamento de curva futura aqui com QuantLib
    return [a.to_dict() for a in ativos]


def processar_futuros_di(insumos):
    ativos = montaAtivosD1(insumos)
    curvaPrazos = []

    for ativo in ativos:
        try:
            vencimento = ativo['Vencimento']
            ultimo_preco = Decimal(ativo['Ultimo_Preco'])
            if isinstance(vencimento, str):
                vencimento = datetime.strptime(vencimento, "%Y-%m-%d").date()
            du = ContaDiaUtil(vencimento)
            pu = taxa_para_pu(ultimo_preco, du)
            resultado = {
                'Nome': ativo['Nome'],
                'Vencimento': vencimento,
                'DU': du,
                'PU': pu
            }
            curvaPrazos.append(resultado)
        except Exception as e:
            print(f"Erro ao processar ativo {ativo}: {e}")

    curvaPrazos.sort(key=lambda x: x['Vencimento'])

    curvaInterpolada = interporlador_pu(curvaPrazos)
    
    return curvaInterpolada