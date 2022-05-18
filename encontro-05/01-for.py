"""""
How Bootcamps - Stone - código[s]
Data: 08/03/2022
Enunciado: Estrutura de repetiçao(for e while)
"""

#Criando um dicionário vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento = dict()

numero_alunos = int(input("Quantos alunos serão cadastrados?"))
numero_notas = int(input("Quantas notas por aluno?"))

for _ in range(numero_alunos):

    nome = input("Digite o nome do aluno: ")

    fechamento [nome] = []

    for _ in range(numero_notas):

        nota = int(input(f"Digite a nota do {nome}: "))

        fechamento[nome].append(nota)
    
for aluno, notas in fechamento.items():

    media = sum(notas) / len(notas)
    print(f"A média do aluno {aluno} foi {media}!")