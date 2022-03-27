""""
How Bootcamp - Stone - /código[s]
Data: 24/02/2022
Enunciado: Estrutura condicional (if, else, elif)
o que é uma condição? - operação que retorna um valor booleano (true - false)
"""

aluna = "Ludmila Timoteo"

notas = []

notas.append(float(input("Digite a primeira nota: ")))

notas.append(float(input("Digite a sgunda nota: ")))

notas.append(float(input("Digite a terceira nota: ")))

nota_media =  sum(notas) / len(notas)

nota_minima_aprovacao = 7
nota_minima_rec = 6

if nota_media >= nota_minima_aprovacao:
    status = "Aprovado"
elif nota_media >= nota_minima_rec:
    
    #Chance de eliminar a nota menos alta
    nota_minima = min(notas)
    #Índice da nota mínima na lista
    nota_minima_indice = notas.index(nota_minima)
    #Eliminando a nota menos alta através do seu índice
    notas.pop(nota_minima_indice)
    #Recalcula a média
    notas_media = sum(notas) / len (notas)

    #Define o status do aluna com a nova média:
    if nota_media >= nota_minima_aprovacao:
        status = f"aprovado com {len(notas)}"
    else: 
        status = "recuperaçao"
#Se nao entrar em nenhuma das condiçoes acima, o aluna estará reprovado. 
else: 
    status = "reprovado"

#Arredonda a média para 2 casas decimais
nota_media_arred = round(nota_media, 2)

print(f"\nA media da aluna {aluna} é {nota_media_arred} e o status é {status}")

