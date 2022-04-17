""""
Exercício 02
"""
def forma_triangulo(a: int, b: int, c: int) -> bool:
    """
    Verifica se os lados de um triangulo são maiores que 0 e
    se algum lado é maior que a soma dos outros dois lados.
    """
    zero_ou_nagativos = a <= 0 or b <= 0 or c <=0

    lado_maior_que_soma_dos_outros = a > b + c or b > a + c or c > a + b

    if zero_ou_nagativos or lado_maior_que_soma_dos_outros:
        return False
    
    return True

print(f"É possível formar um triângulo com os lados 3, 4 e 5 ? Resposta: {forma_triangulo(3,4,5)}")
print(f"É possível formar um triângulo com os lados 1, 1 e 10 ? Resposta: {forma_triangulo(1,1, 10)}")
print(f"É possível formar um triângulo com os lados 0, 4 e 5 ? Respota: {forma_triangulo(0,4,5)}")
