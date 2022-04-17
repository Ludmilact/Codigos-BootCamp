"""
Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário,
mas, dessa vez, apenas os números ímpares.
"""

numero_usuario = int(input("Digite um número: "))
inicio = 1 
while inicio <= numero_usuario:
    print(inicio)
    inicio = inicio + 2