""""
Escreva um programa que pergunte a velocidade do carro de um usuário.
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
"""

velocidade_carro_usuario = int(input("Digite a velocidade do carro: "))
if velocidade_carro_usuario > 80:
    multa = (velocidade_carro_usuario - 80) * 5 
    print(f"Você foi multado em R$ {multa}!")
elif velocidade_carro_usuario <= 80:
    print("Sua velocidade é permitida.")
