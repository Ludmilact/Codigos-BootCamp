""""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Enunciado: Introduçao aos tipos de dados - sets

Característica dos sets:
Conjuntos matemáticos - nao há como acessar por posiçao (posicoes sao aleatórias)
Elementos únicos, exclusivos, sem repetiçao.
"""

#Percebam que é diferente de um dicionário, pois dict tem {} : e, separando as chaves e valores

from math import factorial


conjunto_a = {1,2,3,4,5,6,7}
print(f"Conjunto A: {conjunto_a}")

#Podemos usar a funçao set() para transformar outros objetos em um set
aluna = set("Ludmila") #Transformando uma string para um set (sem letras repetidas)

letras_aleatorias = set("Alimduleas")

#----------------------------------------------------------------------------------------------

###COMPARANDO CONJUNTOS!

#Pergunta 1: Quais letras em comum temos em "aluna" e "letras_aleatorias?"
print(f"Respostas 1: {aluna.intersection(letras_aleatorias)}")

#Pergunta 2: Quais letras temos em "aluna" que nao estao em letras_aleatorias?
print(f"Resposta 2: {aluna - letras_aleatorias}")

#Pergunta 3: Quais letras temos em "letras_aleatorias" que nao estao em "aluna?"
print(f"Resposta 3: {letras_aleatorias - aluna}")

#Pergunta 4: Quantas letras nao repetidas temos ao total, quando consideramos "Aluna" e "letras_aleatorias"?
print(f"Resposta 4: {len(aluna.union(letras_aleatorias))}")

#Pergunta 5: Quais letras estao ou em "letras_aleatorias" ou em "aluna"
print(f"Resposta 5: {aluna.symmetric_difference(letras_aleatorias)}")

#Pergunta 6: A letra A está em "aluna"
print(f"Resposta 6: {'a'in aluna}")

print(f"Resposta 7: {letras_aleatorias.issubset(aluna)}")