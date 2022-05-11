"""
How Bootcamps - Stone - /código[s]
Data: 14/04/2022
"""

from pessoas import Funcionario

funcionario1 = Funcionario("Ludmila", "Timoteo", 100)

funcionario2 = Funcionario("Bruno", "Lautenschlager", 100)

funcionario1.dar_aumento()

print(funcionario1.salario_atual)