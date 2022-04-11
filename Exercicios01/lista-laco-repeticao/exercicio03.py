""""
Exercício 03
"""

preco_final = 0.0
continuar = True

print("Digite a idade dos visitantes: ")
print("Precione a tecla 'enter' para encerrar!")

while continuar:
    idade = input("Digite uma idade para continuar: ")

    if not idade:
        continuar = False

    else:
        idade = int(idade)

        if 3 <= idade <= 12:
            preco_final += preco_final + 14
        elif 13 <= idade <= 64:
            preco_final += preco_final + 23
        elif 65 <= idade:
            preco_final += preco_final + 18

print(f"O preco final do grupo é R$ {preco_final:.2f}")