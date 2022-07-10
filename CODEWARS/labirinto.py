

from operator import pos
from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

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


def movimento(posicao: tuple, direcao: list):
    calculo_coordenadas_movimento = [posicao[0] + direcao[0], posicao[1] + direcao[1]]

    LABIRINTO[calculo_coordenadas_movimento[0]][calculo_coordenadas_movimento[1]] = ROBO
    
    LABIRINTO[posicao[0]] [posicao[1]] = CAMINHO_PERCORRIDO
    
    return calculo_coordenadas_movimento

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    calculo_coordenadas_possivel_direcao = [posicao[0] + direcao[0], posicao[1] + direcao[1]]

    coordenada_no_labirinto = LABIRINTO[calculo_coordenadas_possivel_direcao[0]][calculo_coordenadas_possivel_direcao[1]]
    
    if coordenada_no_labirinto == PAREDE:
        return False
    elif coordenada_no_labirinto == CAMINHO_PERCORRIDO:
        return False
    elif coordenada_no_labirinto == CAMINHO_LIVRE:
        return True
    elif coordenada_no_labirinto == SAIDA:
        return True


def main():
    POSICAO_PERCORRIDA = [] 
    POSICAO_INICIAL = [9,6]
    POSICAO_FINAL = [9,18]
    POSICAO_MAXIMA = [9,19]
    
    posicao_inicial_usuario = (input("Digite uma posição inicial para o Robo: "))
    
    posicao_inicial_usuario = posicao_inicial_usuario.split(",")

    posicao_inicial_usuario[0] = int(posicao_inicial_usuario[0])

    posicao_inicial_usuario[1] = int(posicao_inicial_usuario[1])

    # #converter string para vetor
    # if  posicao_inicial_usuario[0] > POSICAO_MAXIMA[0]:
    #     return 
    # elif posicao_inicial_usuario[1] > POSICAO_MAXIMA[1]:
    #     return
    # elif LABIRINTO[posicao_inicial_usuario[0]] [posicao_inicial_usuario[1]] == PAREDE:
    #     print("Posição informada é invalida") 

    possiveis_direcoes = [ESQUERDA, DIREITA, CIMA, BAIXO]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO #colocando robo no mapa

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL 

    contador_direcoes = 0 # para saber se ele tem que voltar uma casa ou não
    
    # While para fazer um loop novamente até encontrar a saída
    while POSICAO_ATUAL != POSICAO_FINAL:
        
        # for para verificar quais das direçoes é possivel ir
        for direcao in possiveis_direcoes:
            if contador_direcoes > 3:
                LABIRINTO[POSICAO_PERCORRIDA[-1][0]] [POSICAO_PERCORRIDA[-1][1]] = CAMINHO_PERCORRIDO #onde o robo travou
                POSICAO_PERCORRIDA.pop()
                POSICAO_ATUAL = POSICAO_PERCORRIDA[-1] #possicao atual é igual a última possicao percorrida
                LABIRINTO[POSICAO_ATUAL[0]] [POSICAO_ATUAL[1]] = ROBO 
                contador_direcoes = 0
                break

            contador_direcoes += 1
            
            # passo a possição atual e a direção da vez do "for" para a funçao "verifica_movimento" que verifica se o mov. é possivel
            if verifica_movimento(POSICAO_ATUAL, direcao): 
                POSICAO_ATUAL = movimento(POSICAO_ATUAL, direcao)
                POSICAO_PERCORRIDA.append(POSICAO_ATUAL) #coloca a posição movimentada na lista
                contador_direcoes = 0
                print_labirinto()
                sleep(1)
    
    print("Parabéns, você saiu do labirinto")
                

if __name__ == "__main__":
    main()
