"""
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""
salario = int(input("Digite o valor do salario: "))
aumento = float(input("Digite a porcentagem do aumento: "))

calculo_porcentagem = salario * aumento / 100

salario_com_aumento = salario + calculo_porcentagem

print("Um aumento de %5.2f %% em um salário de R$ %7.2f" % (aumento, salario))
print("é igual a um aumento de R$ %7.2f" % calculo_porcentagem)
print("Resultado em um novo salário de R$ %7.2f" % salario_com_aumento)