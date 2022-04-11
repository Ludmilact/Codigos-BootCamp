""""
Exercício 01 - Laços e repetiçao
"""

lista_valores = []

while 0 not in lista_valores:
    valor = float(input("Digite um valor (ou digite 0 para encerrar a entrada de novos valores): "))

    if valor != 0:
        lista_valores.append(valor)
    else:
        break

if not lista_valores:
    print("Nao há valores na lista!")
else: 
    print(f"A média dos valores calculados é: {sum(lista_valores) / len(lista_valores)}")
