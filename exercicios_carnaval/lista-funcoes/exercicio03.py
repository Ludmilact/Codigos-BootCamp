""""
Exercicio 03
"""

def inverte_numero(numero: int) -> int:
    return int( "".join( reversed( str(numero) ) ) )

print(inverte_numero(124))
