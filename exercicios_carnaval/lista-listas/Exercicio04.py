""""
Exercicio 05
"""

meses = (
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)

temperaturas = []
for mes in meses:
    temperatura = float(input(f"Digite a temperatura (C) do mês de {mes}: "))

    temperaturas.append(temperatura)

    media_anual_temp = round(sum(temperaturas) / len(temperaturas), 2)

    print(f"Meses com a temperatura acima da média anual de {media_anual_temp} C:")

    for indice, temp in enumerate(temperaturas):

        if temp > media_anual_temp:
            
            print(f"{indice+1} - {meses[indice]}")