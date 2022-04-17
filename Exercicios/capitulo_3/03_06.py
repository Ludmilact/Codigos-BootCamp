""""
Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. 
Para ser aprovado, todas as médias do aluno devem ser maiores que 7. 
Considere que o aluno cursa apenas três matérias, 
e que a nota de cada uma está armazenada nas seguintes variáveis:
matéria1, matéria2 e matéria3.
"""

materia1 = 70
materia2 = 50
materia3 = 70

resultado_aprovacao = materia1 >= 70 and materia2 >= 70 and materia3 >= 70 

print(resultado_aprovacao)