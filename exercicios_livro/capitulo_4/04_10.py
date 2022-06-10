"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação:
R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
"""

quantidade_kWh = int(input("Digite a quantidade de kWh consumida: "))
instalacao = str(input("Digite o tipo de instalação, sendo 'R' para residências, 'I' para indústrias e 'C' para comércios."))

if instalacao == "R" and quantidade_kWh < 500:
    total_pagamento = quantidade_kWh * 0.40
elif instalacao == "R" and quantidade_kWh > 500:
    total_pagamento = quantidade_kWh * 0.65
elif instalacao == "C" and quantidade_kWh < 1000:
    total_pagamento = quantidade_kWh * 0.55
elif instalacao == "C" and quantidade_kWh > 1000:
    total_pagamento = quantidade_kWh * 0.60
elif instalacao == "I" and quantidade_kWh < 5000:
    total_pagamento = quantidade_kWh * 0.55
elif instalacao == "I" and quantidade_kWh > 5000:
    total_pagamento = quantidade_kWh * 0.60
else:
    print("Valor inválido!")

print(f"R${total_pagamento}")