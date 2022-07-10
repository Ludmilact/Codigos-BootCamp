""""
Exercicio 4
"""

entradaDicionario = {1: "vermelho", 2: "azul", 3: "marrom"}

saida = dict()

for chave, valor in entradaDicionario.items():
    saida[chave] = len(valor)
print(saida)