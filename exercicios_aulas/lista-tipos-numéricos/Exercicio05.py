""""
Exercicio 05
"""

numero = input("Digite um número de 4 dígitos: ")

while(len)(numero) != 4 or not numero.isnumeric():

    numero = input("Número inválido! Digite um número válido de 4 dígitos: ")

soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])

print(f"{numero[0]} + {numero[1]} + {numero[2]} + {numero[3]} = {soma}")