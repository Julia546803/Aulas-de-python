



def fibonacci (n):
    if n <= 2:
        return n - 1

    a = 0
    b = 1
    c = 0

    for _ in range (2, n):
        c = a + b
        a, b = b, c
    return c

print(fibonacci(5))


def calcular_fatorial (numero):
    if numero < 2:
        return 1

    return numero * calcular_fatorial(numero - 1)

print(calcular_fatorial(5))

def calcular_fatorial (numero):
    if numero < 2:
        return 1

    fat = 1
    for i in range (numero, 1, -1):
        fat = fat * i

    return fat

print(calcular_fatorial(0))