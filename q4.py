def calcular_porcentagem_por_estado(faturamento_estado):
    total_faturamento = sum(faturamento_estado.values())
    percentagens = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estado.items()}
    return percentagens

faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

print(calcular_porcentagem_por_estado(faturamento_estado))
