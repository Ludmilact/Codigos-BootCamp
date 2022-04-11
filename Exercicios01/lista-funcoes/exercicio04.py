""""
Exercicio 04
"""

# def recebe_string = (input("Digite uma palavra: "))
#     return recebe_string.
# ...

from random import shuffle

def embaralha_string(texto_entrada: str) -> str:
    """
    Recebe uma string e embaralha suas letras e a retorna.
    """
    lista_string = []
    for letra in texto_entrada:
        lista_string.append(letra.upper())
    
    shuffle(lista_string)
    texto_embaralhado = "".join(lista_string)
    return texto_embaralhado

print(embaralha_string("Ludmila"))