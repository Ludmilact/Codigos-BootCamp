"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, de 15%.
"""

salario_funcionario = int(input("Digite o valor do salário: "))
percentual_aumento = 0.15

if salario_funcionario > 1250:
    percentual_aumento = 0.10

aumento = salario_funcionario * percentual_aumento
print(f"O aumento será de R$ {aumento}")