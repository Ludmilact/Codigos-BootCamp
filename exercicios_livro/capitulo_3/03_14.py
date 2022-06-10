"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

valor_carro_dia = 60
valor_km_rodado = 0.15

quantidade_km_percorridos = (int(input("Digite a quantidade de KM percorridos: ")))
quantidade_dias_aluguel = (int(input("Digite a quantidade de dias que o carro está alugado: ")))

valor_final = quantidade_dias_aluguel * valor_carro_dia + quantidade_km_percorridos * valor_km_rodado

print(f"Total a pagar: R$ {valor_final}")