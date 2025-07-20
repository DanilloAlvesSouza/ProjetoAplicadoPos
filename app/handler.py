import json
from services.curva_service import processar_futuros_di
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

def handler(event, context):
    try:
        for record in event['Records']:
            body = json.loads(record['body'])

            if body.get('Categoria') == 'Futuros_DI':
                insumos = body.get('insumos', [])
                curvaFinalizada = processar_futuros_di(insumos)

                # --- Visualização com matplotlib apenas em ambiente local ---
                if os.environ.get("ENV") == "local":
                    prazos = [p['Vencimento'] for p in curvaFinalizada]
                    valores = [p['PU'] for p in curvaFinalizada]
                    plt.plot(prazos, valores, marker='o')
                    plt.title('Curva de Juros Interpolada')
                    plt.xlabel('Prazo (dias úteis)')
                    plt.ylabel('PU ou Taxa')
                    plt.grid(True)
                    plt.show()
                # ----------------------------------------------------------

            else:
                print("Categoria desconhecida ou não suportada.")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Processamento concluído com sucesso."})
        }

    except Exception as e:
        print("Erro ao processar evento:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Erro no processamento."})
        }
