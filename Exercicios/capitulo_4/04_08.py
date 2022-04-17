"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
"""
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
operacao = str(input("Digite uma operação: "))

if operacao == "+" :
    resultado_operacao = a + b
elif operacao == "-":
    resultado_operacao = a - b
elif operacao == "*":
    resultado_operacao = a * b 
elif operacao == "/":
    resultado_operacao = a / b
elif operacao == "%":
    resultado_operacao = a % b
else:
    print("Operação invalida!")
    resultado_operacao = 0

print(f"O resultado da operação é: {resultado_operacao}")