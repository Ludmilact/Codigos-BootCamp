""""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Henrique J. Branco
Enunciado: Introdução aos tipos de dados(String)
"""

nome = " Ludmila Timoteo "

### Métodos de string com a sintaxe nome.metodo()

print(f"Nome em maiusculo: {nome.upper()}")

print(f"Nome em minúsculo: {nome.lower()}")

print(f"Primeira letra em maiúsculo: {nome.capitalize()}")

#A Atenção às aspas duplas e simples! Comentamos isso na aula!

print(f"Contando quantas vezes a letra 'a' aparece no nome: {nome.count('a')}")

print(f"Removendo espaços em branco no começo e final da string: {nome.strip()}")

print(f"Substituindo meu primeiro nome por algo: {nome.replace('Ludmila', 'ALGO')}")

print(f"Substituindo meu nome por algo: {nome.replace('Ludmila C. Timoteo', 'ALGO')}")

print(f"Separando o nome em partes: {nome.split()}")

###Função len()

print(f"A minha string contém {len(nome)} caracteres")