"""
Exercício 07
"""

listaElementos =  ["Olá", "", "meu", "nome", "", "é", "Ludmila", ""]

lista_sem_str_vazias = []

for item in listaElementos:

    if item:
        lista_sem_str_vazias.append(item)

print(lista_sem_str_vazias)
