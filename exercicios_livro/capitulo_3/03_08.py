""""
Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
"""

metros = float(input("Digite um valor em metros: "))
conversao_metros_em_milimetros = metros * 1000
print("%10.3f metros equivalem a %10.3f milímetros." % (metros, conversao_metros_em_milimetros))