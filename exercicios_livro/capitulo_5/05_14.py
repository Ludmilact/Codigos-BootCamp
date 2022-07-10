"""
Escreva um programa que leia números inteiros do teclado. 
O programa deve ler os números até que o usuário digite 0 (zero). 
No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética
"""

soma = 0 
quantidade = 0

while True: 
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        break
    else: soma = soma + numero
    quantidade = quantidade + 1 
    media = soma / quantidade
print(f"A soma dos {quantidade} números é = {soma} e a média é {media:5.2f}.")
