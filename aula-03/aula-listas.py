""""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Enunciado: Introdução aos tipos de dados - listas
"""

## Listas começam com []

notas = [4, 5, 0, 9, 10]
print(f"\nNotas: {notas}")

notas_tup = (1,2,3,4)
notas = list(notas_tup) 
print(f"\nA variável notas é do tipo: {type(notas)}") 

lista_objetos_variados = ["Ludmila", 1, 10.0, False,[5,5,5]]
print(f"\n A lista `lista_objetos_variados` tem {len(lista_objetos_variados)} elementos")

#------------------------------------------------------------------------------------------------
### ACESSANDO ELEMENTOS DE LISTA COM FATIAMENTO (slicing)

# Acessando o primeiro elemento da lista 
primeiro_elemento = lista_objetos_variados[0]
print(f"\nO primeiro elemento da lista é {primeiro_elemento}")

# Acessando o segundo elemento da lista
segundo_elemento = lista_objetos_variados[1]
print(f"\nO segundo elemento da lista é {segundo_elemento}")

ultimo_elemento = lista_objetos_variados[-1]
penultimo_elemento = lista_objetos_variados[-2]
print(f"\nO último elemento da lista é {ultimo_elemento} e o penúltimo é {penultimo_elemento}")

#------------------------------------------------------------------------------------------------

### MÉTODOS MAIS COMUNS DE LISTA

# Adicionando um objeto inteiro ao final da lista
lista_objetos_variados.append([9,9,9])
print(f"\n O elemento [9,9,9] foi adicionado ao final da lista: {lista_objetos_variados}")

# Adicionando elemento a elemento de um objeto à lista
lista_objetos_variados.extend("Ludmila Custodio Timoteo")
print(f"\nCada letra da string foi adicionado como um elemento à lista: {lista_objetos_variados}")

# Adicionando um objeto inteiro em uma determinada posição
lista_objetos_variados.insert(0, "Index O")
print(f"\nA string foi adicionada na primeira posição da lista, de índice 0: {lista_objetos_variados}")

# Removendo o primeiro elemento encontrado da lista, retorna erro se não encontrar o elemento
lista_objetos_variados.remove([9,9,9])
print(f"\nO objeto [9,9,9] agora foi removido da lista: {lista_objetos_variados}")

# Coletando um elemento da lista e salvando em uma variável a partir de um índice
# O .pop() permite salvar o elemento removido em uma variável, o .remover() não permite!

elemento_coletado = lista_objetos_variados.pop(0)
print(f"\nO elemento no índice 0 foi removido da lista: {lista_objetos_variados}")
print(f"\nO elemento coletado é {elemento_coletado}")

# Ordenando os valores de uma lista
notas.sort() 
print(f"\nNotas ordenadas: {notas}")