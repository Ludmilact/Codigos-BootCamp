"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
quantidade_anos = int(input("Digite os anos para o pagamento da casa: "))

meses = quantidade_anos * 12
prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print("Infelizmente você não pode receber o empréstimo.")
else:
    print(f"Valor da prestação: R$ {prestacao}. Empréstimo liberado!")
