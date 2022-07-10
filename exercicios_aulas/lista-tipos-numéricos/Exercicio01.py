""""
Exercicío 01 
"""

from math import log10


numeroUsuarioA = int(input("Digite um numero inteiro para A: "))
numeroUsuarioB = int(input("Digite um numero inteiro para B: "))

somaAB = numeroUsuarioA + numeroUsuarioB

print(f"\n A soma de A + B é: {somaAB}\n")

#########################################################

diferencaAB = numeroUsuarioB - numeroUsuarioA

print(f"\n A diferença de B e A é: {diferencaAB}\n")

#########################################################

produtoAB = numeroUsuarioA * numeroUsuarioB

print(f"\n O produto de A e B é: {produtoAB}\n")

#########################################################

divisaoAB = numeroUsuarioA / numeroUsuarioB 

print(f"\n O quociente de A dividido por B é: {divisaoAB} \n")

#########################################################

restoDivisaoAB = numeroUsuarioA % numeroUsuarioB

print(f"\n O resto da divisão de A por B é: {restoDivisaoAB}\n")

#########################################################

resultadoLog10 = log10(numeroUsuarioA)

print(f"\n O logo10 de A é: {resultadoLog10}\n")

#########################################################

resultadoElevado = numeroUsuarioA ** numeroUsuarioB

print(f"\n O resultado de A elevado a B é: {resultadoElevado}\n")