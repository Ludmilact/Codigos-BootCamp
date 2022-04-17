""""
Escreva um programa que converta uma temperatura digitada em °C em °F. 
A fórmula para essa conversão é:
"""
C = float(input("Digite a temperatura em C: "))
F = (9 * C / 5) + 32
print("%5.2fC é igual a %5.2f F" % (C, F))
