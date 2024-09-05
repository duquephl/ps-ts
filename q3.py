#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

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
