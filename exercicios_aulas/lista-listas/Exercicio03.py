""""
Exercicio 3
"""

listaNumerosInteiros = [2, 6, 26, 266, 2666, 26666]

maior = max(listaNumerosInteiros)
menor = min(listaNumerosInteiros)

posicao_maior = listaNumerosInteiros.index(maior)
posicao_menor = listaNumerosInteiros.index(menor)

print(f"O maior elemento é o {maior} e está na posição {posicao_maior}")
print(f"O menor elemento é o {menor} e está na posicao {posicao_menor}")