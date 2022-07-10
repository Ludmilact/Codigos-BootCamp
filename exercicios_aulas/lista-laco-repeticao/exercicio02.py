"""
Exercício 02
"""

print("C -> F")

for temperatura_celcius in range(10,101,10):
    temperatura_fahrenheit = int(temperatura_celcius * 9 / 5 + 32)
    print(f"{temperatura_celcius} -> {temperatura_fahrenheit}")