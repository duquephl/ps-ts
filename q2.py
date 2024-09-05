def pertence_fibonacci(numero):
    sequencia_fibonacci = [0, 1]
    while sequencia_fibonacci[-1] < numero:
        proximo_valor = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
        sequencia_fibonacci.append(proximo_valor)
    
    if numero in sequencia_fibonacci:
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")

pertence_fibonacci(22)
