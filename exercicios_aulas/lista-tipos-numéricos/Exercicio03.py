""""
Exercicío 3
"""

lado1Triangulo = int(input("Digite o primeiro lado do triângulo: "))
lado2Triangulo = int(input("Digite o segundo lado do triângulo: "))
lado3Triangulo = int(input("Digite o teceiro lado do triângulo: "))

calculoTriangulo = (lado1Triangulo + lado2Triangulo + lado3Triangulo) / 2

areaTriangulo = (calculoTriangulo * (calculoTriangulo - lado1Triangulo) * (calculoTriangulo - lado2Triangulo) * (calculoTriangulo - lado3Triangulo)) ** 0.5

print(f"\n A área do triângulo é: {areaTriangulo:.2f}\n")
