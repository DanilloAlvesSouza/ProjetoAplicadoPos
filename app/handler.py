import json
from services.curva_service import processar_futuros_di

def handler(event, context):
    try:
        for record in event['Records']:
            body = json.loads(record['body'])  # body ainda é uma string JSON

            if body.get('Categoria') == 'Futuros_DI':
                insumos = body.get('insumos', [])
                resultadoPrazoCalculado = processar_futuros_di(insumos)
                print("Resultado do processamento:", resultadoPrazoCalculado)
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
