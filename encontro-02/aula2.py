""""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Henrique Branco
Enunciado: Introdução à sintaxe e tipos de dados (int, float)
"""

aluna = "Ludmila"

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a teceira nota: "))

media = (nota1 + nota2 + nota3) / 3

media_arred = round(media,2)

print(f"\nA aluna {aluna} ficou com a média {media_arred}")
