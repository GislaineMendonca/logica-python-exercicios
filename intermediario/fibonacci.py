# Gere os N primeiros números da sequência de Fibonacci.

n = int(input("Quantos números da sequência de Fibonacci você quer gerar? "))

a, b = 0, 1
contador = 0

while contador < n:
    print(a)
    a, b = b, a + b
    contador += 1
