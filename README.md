# ProjetoAplicadoPos

## Resumo

Este projeto realiza o processamento de curvas de juros a partir de insumos de contratos futuros DI, utilizando cálculos financeiros e interpolação de preços unitários (PU). A aplicação recebe eventos (payloads) contendo informações de ativos, processa os dados para calcular prazos úteis, converte taxas em PU e gera curvas interpoladas para análise de risco e precificação.

O fluxo principal é:
- Recebimento de eventos com dados de ativos futuros DI.
- Cálculo do número de dias úteis até o vencimento de cada ativo.
- Conversão da taxa de juros em preço unitário (PU).
- Interpolação dos PUs ao longo dos prazos para construção da curva.
- Retorno da curva processada.

## Estrutura

- `app/handler.py`: Função principal que orquestra o processamento dos eventos.
- `app/services/curva_service.py`: Processamento dos ativos e construção da curva.
- `app/services/calculos_service.py`: Funções de cálculo financeiro (taxa para PU, fator de juros compostos).
- `app/services/interpolador.py`: Interpolação dos preços unitários.
- `app/Utils/utils.py`: Utilitários para cálculo de dias úteis e feriados.
- `app/models/ativo.py`: Modelo de dados para os ativos.
- `app/mock_payload.json`: Exemplo de payload para testes locais.
- `app/main.py`: Script para execução local do processamento.

## Bibliotecas Necessárias

As principais dependências estão listadas em [app/requirements.txt](app/requirements.txt):

- `numpy`: Operações matemáticas e vetoriais.
- `scipy`: Interpolação de dados.
- `decimal`: Precisão em cálculos financeiros (já incluída na biblioteca padrão do Python).
- `pytest`: (opcional, para testes unitários).
- `matplotlib`: (opcional, para visualização gráfica).

Para instalar as dependências principais, execute:

```sh
pip install -r app/requirements.txt
```