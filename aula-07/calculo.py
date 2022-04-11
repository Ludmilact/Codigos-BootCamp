""""
How Bootcamps - Stone - /código[s]
Data:15/03/2022
Enunciado: módulos
"""
def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """" Calcula a media ponderada """

    if not pesos:
        pesos = (1,) * len(valores)

    numerador = 0

    denominador = sum(pesos)

    for valor, peso in zip(valores, pesos):
        numerador = numerador + valor * peso
    return numerador / denominador