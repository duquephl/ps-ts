def calcula_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k = k + 1
        soma = soma + k
    return soma

print(calcula_soma(10))