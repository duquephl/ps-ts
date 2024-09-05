#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

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
