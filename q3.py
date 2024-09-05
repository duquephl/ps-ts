import json

def analisar_faturamento(faturamento_json):
    faturamento = json.loads(faturamento_json)
    
    faturamento_valido = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
    if not faturamento_valido:
        return "Não há dados de faturamento válidos."
    
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    media = sum(faturamento_valido) / len(faturamento_valido)
    
    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media)
    
    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_da_media": dias_acima_da_media
    }

faturamento_json = '''
[
    {"dia": 1, "valor": 1000},
    {"dia": 2, "valor": 1500},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 2000}
]
'''

print(analisar_faturamento(faturamento_json))
