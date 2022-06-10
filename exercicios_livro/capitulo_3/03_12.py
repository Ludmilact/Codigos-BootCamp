"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

distancia = float(input("Digite a distancia em KM: "))
velocidade = float(input("Digite a velocidade média: "))

tempo = distancia / velocidade
print("O tempo estimado é de %5.2f horas" % tempo)

tempo_s = int(tempo * 3600) # conversão de horas para segundos
horas = int(tempo_s / 3600) # parte inteira
tempo_s = int(tempo_s % 3600) # o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print("%05d:%02d:%02d" % (horas, minutos, segundos))