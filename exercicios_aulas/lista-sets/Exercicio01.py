""""
Exercicio 01 - Sets
"""

alunos_matriculados_ingles = {
"João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral",
}

alunos_matriculados_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva",
}
print(f" (1) O total de alunos matriculados é: {len(alunos_matriculados_ingles.union(alunos_matriculados_frances))}", end ="\n\n")
print(f" (2) A quantidade de alunos matriculados em inglês é {len(alunos_matriculados_ingles)}. Os alunos são: {alunos_matriculados_ingles}", end ="\n\n") 
print(f" (3) A quantidade de alunos matriculados em francês é {len(alunos_matriculados_frances)}. Os alunos são: {alunos_matriculados_frances}", end="\n\n")
print(f" (4) A quantidade de alunos matriculados em ambos os cursos é {len(alunos_matriculados_ingles.intersection(alunos_matriculados_frances))}. Os alunos matriculados são - {alunos_matriculados_frances.intersection(alunos_matriculados_ingles)}", end ="\n\n")
print(f" (5) Existem {len(alunos_matriculados_ingles.symmetric_difference(alunos_matriculados_frances))} matriculados apenas em uma disciplina.")