"""""
Exercício 04
"""

pi = 0 

for aproximadamente in range (15):
    if aproximadamente == 0:
        pi += 3
        continue

    dobro_aproximadamente = aproximadamente * 2
    denominador = dobro_aproximadamente * (dobro_aproximadamente + 1) * (dobro_aproximadamente + 2)

    if aproximadamente % 2 != 0:
        pi += 4 / denominador
    else:
        pi -= 4 / denominador

print(f"O número pi com 15 aproximaçoes é {pi}")