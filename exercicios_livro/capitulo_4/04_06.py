"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, 
e R$ 0,45 para viagens mais longas.
"""

distancia_em_km = int(input("Digite a distância que deseja percorrer em km: "))

preco_passagem = 0.50

if distancia_em_km > 200:
    preco_passagem = 0.45

valor_passagem = distancia_em_km * preco_passagem

print(f"O valor da passagem será de {valor_passagem}")