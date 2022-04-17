""""
Exercicio 03
"""

nivelSonoroUsuario = int(input("Escreve um valor de nível sonoro em decibéis: "))

if nivelSonoroUsuario == 130:
    print("Valor sonoro correspondente a uma britadeira.")
elif 106 < nivelSonoroUsuario < 130:
    print("Valor sonoro entre britadeira e cortador de grama.")
elif nivelSonoroUsuario == 106:
    print("Valor sonoro correspondente a um cortador de grama.")
elif 70 < nivelSonoroUsuario < 106:
    print("Valor sonoro entre um cortador de grama e um despertador.")
elif nivelSonoroUsuario == 70:
    print("Valor sonoro de um despertador.")
elif 40 < nivelSonoroUsuario <70:
    print("Valor sonoro entre despertador e cômodo silencioso.")
elif nivelSonoroUsuario < 70:
    print("Valor sonoro abaixo de um cômodo silencioso.")
else:
    print("Valor sonoro acima de uma britadeira.")