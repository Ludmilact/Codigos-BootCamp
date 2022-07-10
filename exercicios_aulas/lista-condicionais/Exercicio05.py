""""
Exercicio 05 - Condicionais
"""

from curses.ascii import isalpha
from turtle import Turtle


placa_usuario = (input("Digite a identificaçao de uma placa veicular: "))

if len(placa_usuario) != 8:
    placa_valida = False
else: 
    letras_placa = placa_usuario[:3]
    numeros_placa = placa_usuario[-4:]
    traco_placa = placa_usuario[3]

    if (letras_placa.isalpha()
        and letras_placa.isupper()
        and numeros_placa.isdigit()
        and traco_placa == "-"
    ):
    
        placa_valida = True

    else:
        placa_valida = False

print(f"A placa {placa_usuario} é valida ? Resp: {placa_valida}")