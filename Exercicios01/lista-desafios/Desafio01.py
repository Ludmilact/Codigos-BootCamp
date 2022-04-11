""""
Desafio - 01
"""

import random

numero_sorteado = random.randint(0,100)

print (numero_sorteado)

numero_usuario = (int(input("Informe um número entre 1 e 100: ")))

if numero_usuario >= 1 and numero_usuario <= 100:
    numero_usuario = True
else:
    numero_usuario = False

print(input("Digite um número entre 1 e 100: "))

###TERMINAR###