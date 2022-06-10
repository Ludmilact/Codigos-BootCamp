"""
Escreva um programa para calcular a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. 
Exiba o total em dias.
""" 

cigarros_por_dia = (int(input("Digite a quantidade de cigarros consumidos por dia: ")))
cigarros_anos = (int(input("Digite a quantidade de anos de consumo: ")))

minutos_em_anos = cigarros_anos * 365 * cigarros_por_dia * 10
reducao_em_dias = minutos_em_anos / (24 * 60)
print(f"Reduçao do tempo de vida em {reducao_em_dias} dias")
