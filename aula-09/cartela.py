"""Modulo com funções e variáveis para cartela de bingo"""

from collections import defaultdict
from email.policy import default
from pyexpat.errors import XML_ERROR_INCOMPLETE_PE
from random import randint, seed
from xml.dom.minidom import CharacterData

#aleatoriedade da cartela
seed(1)

LETRAS = ("B", "I", "N", "G", "O")

def min_max(letra:str) -> tuple[int]:
    """Gera o valor mínimo e máximo para a letra dada.

    Args:
    letra(str): Letra de input
    
    Returns:
    tuple[int]: valores mínimo e máximo
    """ 
    intervalo = {"B": (1,15), "I": (16, 30), "N": (31, 45), "G": (46, 60), "O": (61, 75)}

    minimo, maximo = intervalo[letra][0], intervalo[letra][1]

    return minimo, maximo

#Passo numero 0
def gerar() -> defaultdict [str, list[int]]:
    """ Gera uma cartela com 5 numeros aleatorios para cada letra."""
 
    cartela = defaultdict(list)

    for letra in LETRAS:
        #Coletar o número mínimo e máximo de cada letra
        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5:
            #gerar um numero aleatorio
            num_aleatorio = randint(minimo, maximo)

            if num_aleatorio in cartela[letra]:
                continue 

            cartela[letra].append(num_aleatorio)

            cartela[letra].sort()

    return cartela
    
#Passo número 1
def imprime(cartela: dict[str, list[int]]) -> None:
    """Formata a cartela para imprimir na tela
    
    Args:
        cartela (dict[str, list[int]]) : cartela de entrada
    """
    print("B  I  N  G  O")
    
    # Para cada linha ele imprime os elementos daquela linha na tela
    for linha in range(5):

        # Gera a lista de elementos já formatada
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]

        #Junta a lista de strings para impressão com uma `,`
        string = ",".join(lista_str)

        print(string)

#Passo número 2
def marca_numero(cartela: defaultdict, letra: str, numero: int, caracter: str):
    #Coletar o índice da lista do número sorteado
    indice = cartela[letra].index(numero)

    cartela[letra][indice] = caracter 

    return cartela

#Passo número 2:
def numero_existe(cartela, letra, numero):
    if numero in cartela[letra]:
        print("Você acertou um número!")
        return True
    print("Você errou!")
    return False
