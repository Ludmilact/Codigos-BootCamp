""""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Enunciado: Estrutura de repetiçao (for e while)
"""

#Criando um dicionário vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento  = dict()

#Recebe o nome do usuário
nome = (input("Digite o nome do aluno: "))

#Inicia o dicionário com o nome do aluno com chave e uma lista vazia
fechamento[nome] = []

#Inicializa a condiçao para entrar na repetiçao while
condicao = "S"

while condicao == "S": 

    #Le uma nota do usuario
    nota = int(input("Digite uma nota: "))

    #Coloca essa nota na lista
    fechamento[nome].append(nota)

    #Pergunta se o usuário quer cadastrar mais notas (atualiza a condicao)

    condicao = input("Deseja entrar com mais uma nota? S ou N?").upper()

    #Se a condicao tiver uma unica letra e for "S"
    if len(condicao) == 1 and condicao == "S":

        #continua o laço de repetiçao  
        continue

    #Caso a condiçao tenha uma letra e for "N"
    elif len(condicao) == 1 and condicao == "N":

        break
    else:
        print("Condicao inválida! Digite uma condicao válida!")

        #Le novamente a condiçao
        condicao = input("Deseja entrar com mais uma nota? S ou N?")
