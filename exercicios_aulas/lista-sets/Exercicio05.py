""""
Exercicio 5
"""


entrada = {"Theodoro":20, "Marcio" : 50, "Junior": 80}

valores = list(entrada.values())

valor_maximo = max(valores)
valor_minimo = min(valores)

indice_maximo = valores.index(valor_maximo)
indice_minimo = valores.index(valor_minimo)

print(f"Nota máxima -> {list(entrada.keys())[indice_maximo]}:{valor_maximo}")
print(f"Nota minima -> {list(entrada.keys())[indice_minimo]}:{valor_minimo}")