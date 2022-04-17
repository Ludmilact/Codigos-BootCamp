""""
Exercicio 04 - Condicionais
"""

ano_usuario = int(input("Digite um ano com 4 digitos: "))

if ano_usuario % 400 == 0:
    ano_bissexto = True
elif ano_usuario % 100 == 0:
    ano_bissexto = False
elif ano_usuario % 4 == 0:
    ano_bissexto = True
else: ano_bissexto = False
 
print(f"O ano {ano_usuario} é bissexto? {ano_bissexto}")