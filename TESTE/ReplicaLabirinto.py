
from CODEWARS.labirinto import CAMINHO_PERCORRIDO


PAREDE = "#"
CAMINHO_LIVRE = " "
ROBO = "4"
SAIDA = "S"
CAMINHO_PERCORRIDO = "2"

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#']
]

def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")

# passo dois parametros para movimento, a direcao e a posicao
# a posicao é tupla e a direcao é list
#  faco uma viavel da classe para somar o valor da posicao ao valor da direcao [0]+[1]
# depois acesso o labirinto para passar a minha variavel de ambiente que sera composta de um vetor [0][1]
# com dois valores e atribuo isso ao Robo, com isso estou falando onde o robo esta no lab.
# depois acesso meu labirinto, passo a posicao [0][1] e atribuo isso ao meu caminho percorrido
# retorno no fim da funcao - calculo_coordenadas_movimento

def movimento(posicao: tuple, direcao: list):
    calculo_coordenadas_movimento = [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    
    LABIRINTO[calculo_coordenadas_movimento[0]][calculo_coordenadas_movimento[1]] = ROBO

    LABIRINTO[posicao[1]] [posicao[2]] = CAMINHO_PERCORRIDO

    return calculo_coordenadas_movimento

# funcao que valida se o movimento pode ser efetuado
# variavel calculo_coordenadas_possivel_direcao passando as duas posicoes [0] [1] 
# e as duas direcoes [0][1]
#  depois passar isso para o labirinto (aqui já serao apenas dois valores [0] e [1] pq ja foram somados em cima)
# fazer if para validar se a coordenada_no_labirinto pode acontecer(parede, caminho_percorido,caminho_livre, saida)

def verifica_movimento(posicao:tuple, direcao: list) -> bool:
    calculo_coordenadas_possivel_direcao = [posicao [0]] + [direcao[0]] [posicao[1]] + [direcao[1]]

    coordenada_no_labirinto = (LABIRINTO[calculo_coordenadas_possivel_direcao[0]] + [calculo_coordenadas_possivel_direcao[1]])

    if coordenada_no_labirinto == PAREDE:
        return False
    elif coordenada_no_labirinto == CAMINHO_PERCORRIDO:
        return False
    elif coordenada_no_labirinto == CAMINHO_LIVRE:
        return True
    elif coordenada_no_labirinto == SAIDA:
        return True

# variaveis posicao_percorida - para fazer uma lista vazia
# posicao inicial - chumbando onde é a posicao inicial do robo
# posicao final - onde fica a saida
# posicao maxima - range do labirinto
# fazer lista com posiveis direcoes 
# colocar o robo no mapa
#printar labirinto
# passar posicao atual igual a posicao inicial
#fazer a variavel contador de direcoes e inicializa-la com zero
#depois comeca o while for if...

def main():
    POSICAO_PERCORIDA = []
    POSICAO_FINAL = [9,9]
    POSICAO_INICIAL = [9,12]
    POSICAO_MAXIMA = [9,14]

    possiveis_direcoes = [ESQUERDA,DIREITA, CIMA, BAIXO]

    LABIRINTO[POSICAO_INICIAL] = ROBO
     
    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    contador_direcoes = 0
    