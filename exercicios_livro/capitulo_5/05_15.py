"""
Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
Utilize a tabela de códigos a seguir para obter o preço de cada produto:

Código Preço
1      0,50
2      1,00 
3      4,00
5      7,00
9      8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
"""

apagar = 0
while True:
    codigo_produto = int(input("Digite o código do produto (0 para sair): "))
    total_compras = 0
    if codigo_produto == 0:
        break
    elif codigo_produto == 1:
        total_compras = 0.50
    elif codigo_produto == 2:
        total_compras = 1.00
    elif codigo_produto == 3:
        total_compras = 4.00
    elif codigo_produto == 5:
        total_compras = 7.00
    elif codigo_produto == 9:
        total_compras = 8.00
    else:
        print(f"Código inválido")
    if total_compras != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (total_compras * quantidade)
print(f"Total a pagar R${apagar:8.2f}")

