""""
Exercicio 03 - Sets
"""

ordena_dicionarios = {"Matematica" : 40, "Portugues" : 50, "Ingles" : 30, "Espanhol" : 90}

ordemNumerica = dict(sorted(ordena_dicionarios.items(), key = lambda tupla: tupla[1], reverse = True))

print(ordemNumerica)