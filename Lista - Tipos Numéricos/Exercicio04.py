"""
Exercicío 4 e melhorias
"""

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

calculoIMC = (peso / altura**2)

print(f"\n O seu IMC é: {calculoIMC:.2f}")