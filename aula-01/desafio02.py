""""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Henrique J. Branco
Enunciado: Exercício proposto na aula intródutoria para elucidar a criatividade dos alunos
e começarem a obter a percepção do que um código faz. O enunciado será escrito ao final da aula,
ao vivo, após análise dos alunos.
"""

# Desafio 02: o que esse pequeno techo de código faz?

quantidade_km = int(input("Digite a quantidade de quilometros percorridos: "))

quantidade_dias = int(input("Digite quantos dias voce ficou com o carro: "))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = quantidade_km * preco_por_km
preco_total_dia = quantidade_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")
