"""
Escreva um programa que leia dois números. 
Imprima o resultado da multiplicação do primeiro pelo segundo. 
Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
"""
primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número: "))

x = 1
r = 0

while x <= segundo_numero:
    r = r + primeiro_numero
    x = x + 1
    print(f"{primeiro_numero} x {segundo_numero} = {r}")