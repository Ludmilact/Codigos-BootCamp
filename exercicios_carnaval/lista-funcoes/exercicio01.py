""""
Exercicio 01
"""

def calcula_tarifa(distancia_km: float) -> float:
    """
    Calcula a tarifa de taxí sendo R$ 4.00 a taxa base 
    mais R$ 0.25 a cada 140 metros.
    """
    taxa_tarifa = 4
    distancia_metros = distancia_km * 1_000
    valor_tarifa_metros = (distancia_metros / 140) * 0.25
    
    return taxa_tarifa + valor_tarifa_metros

print (f"Para uma distancia de 0,14km (1.400 metros) o valor total da corrida é: {calcula_tarifa(0.14)}") 
