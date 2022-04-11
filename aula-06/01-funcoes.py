""""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Enunciado: funçoes
"""

#Definicao da funcao para calculo da média
#A funcao recebe uma lista como parametro e retorna um float

def calcula_media(lst: list) -> float:
    """" Calcula a media aritmetica """

    return sum(lst) / len(lst)


def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """ Calcula a média ponderada """

    #Se nao for passado o parametro de pesos

    if not pesos:
        pesos = (1,) * len(valores)

    numerador = 0
    denominador = sum(pesos)

    for valor, peso in zip(valores, pesos):

        numerador = numerador + valor * peso

    return numerador / denominador

#Criando um dicionario vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento = dict()

#Recebe do usuario quantos alunos serao cadastrados
numero_alunos = int(input("Quantos alunos serão cadastrados?"))

#Recebe quantas notas por aluno serao cadastradas
numero_notas = int(input("Quantas notas por aluno serão cadastradas?"))

#Laço de repeticao para cadastro de alunos

for _  in range (numero_alunos):
    nome = input("Digite o nome do aluno: ")

    #Cria no dicionario uma chave com o nome do aluno, e o valor sendo uma lista vazia
    fechamento[nome] = []

    #Laco de repeticao para ler as notas do aluno
    for _ in range(numero_notas):

        #Le a nota daquele aluno
        nota = int(input(f"Digite a nota de {nome}: "))
        
        #Coloca a nota na lista
        fechamento[nome].append(nota)

for aluno, notas in fechamento.items():

    media = calcula_media_ponderada(notas)

    print(f"A media do aluno {aluno} foi {media}!")
