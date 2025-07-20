from datetime import date, timedelta

# Lista de feriados nacionais fixos no Brasil (adicione outros se necessário)
FERIADOS_FIXOS = [
    (1, 1),   # Confraternização Universal
    (4, 21),  # Tiradentes
    (5, 1),   # Dia do Trabalho
    (9, 7),   # Independência
    (10, 12), # Nossa Senhora Aparecida
    (11, 2),  # Finados
    (11, 15), # Proclamação da República
    (12, 25), # Natal
]

def eh_feriado(dt):
    return (dt.month, dt.day) in FERIADOS_FIXOS

def ContaDiaUtil(data_futura):
    hoje = date.today()
    dias_uteis = 0
    dia = hoje

    while dia < data_futura:
        if dia.weekday() < 5 and not eh_feriado(dia):  # 0=segunda, 6=domingo
            dias_uteis += 1
        dia += timedelta(days=1)
    return dias_uteis