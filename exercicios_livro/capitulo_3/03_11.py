""""
Faça um programa que solicite o preço de uma mercadoria 
e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""

preco = float(input("Digite o valor da mercadoria: "))
percentual_desconto = float(input("Digite o valor do desconto: "))

calculo_desconto = preco * percentual_desconto / 100
calculo_preco = preco - calculo_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (percentual_desconto, preco))
print("Vale R$ %7.2f." % calculo_desconto)
print("O valor a pagar é de R$ %7.2f" % calculo_preco)
