# Calcule o fatorial de um número usando recursão.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso:
numero = int(input("Digite um número: "))
print("Fatorial de", numero, "é", fatorial(numero))