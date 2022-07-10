""""
Exercicio 2
"""

from tkinter import E

listaEstados = {
    "RR": "Roraima",
    "AP": "Amapá",
    "AM": "Amazonas",
    "PA": "Pará",
    "AC": "Acre",
    "RO": "Rondônia",
    "TO": "Tocantins",
    "MA": "Maranhão",
    "PI": "Piauí",
    "CE": "Ceará",
    "RN": "Rio Grande do Norte",
    "PB": "Paraíba",
    "PE": "Pernambuco",
    "AL": "Alagoas",
    "SE": "Sergipe",
    "BA": "Bahia",
    "MT": "Mato Grosso",
    "DF": "Distrito Federal",
    "GO": "Goiás",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "ES": "Espírito Santo",
    "RJ": "Rio de Janeiro",
    "SP": "São Paulo",
    "PR": "Paraná",
    "SC": "Santa Catarina",
    "RS": "Rio Grande do sul",
}

estado_usuario = (input("Digite um estado: "))
estado_usuario = estado_usuario.upper()

if estado_usuario in listaEstados:
    print(f"Essa sigla corresponde ao estado de: {listaEstados[estado_usuario]}")
else:
    print("Sigla inválida!")