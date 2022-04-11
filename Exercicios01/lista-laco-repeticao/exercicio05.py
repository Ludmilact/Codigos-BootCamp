""""
Exercício 05 
"""
notas = []

nome_atleta = input("Digite o nome do/a atleta: ")
for _ in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

maior_nota = max(notas)

indice_maior_nota = notas.index(maior_nota)
notas.pop(indice_maior_nota)

menor_nota = min(notas)
indice_menor_nota = notas.index(menor_nota)
notas.pop(indice_menor_nota)

print("Resultado final: ")
print(f"Atleta: {nome_atleta}")
print(f"Melhor nota: {maior_nota}")
print(f"Pior nota: {menor_nota}")
print(f"Média: {sum(notas) / len(notas)}")