"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período.
"""
deposito_inicial = int(input("Digite o valor do deposito inicial: "))
taxa_juros = float(input("Digite o valor da taxa de juros: "))
mes = 1
saldo = deposito_inicial
while mes <= 24:
    saldo = saldo + (saldo * (taxa_juros / 100))
    print(f"Saldo do mês {mes} é de R${saldo: 5.2f}.")
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito_inicial: 8.2f}.")


