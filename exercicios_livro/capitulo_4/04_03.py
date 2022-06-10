"""
Escreva um programa que leia três números e que imprima o maior e o menor.
"""

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))

maior = a

if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
menor = a
if b < c and b < a :
    menor = b 
if c < b and c < a :
    menor = c
    
print(f"O menor número é {menor}!")
print(f"O maior número é {maior}!")