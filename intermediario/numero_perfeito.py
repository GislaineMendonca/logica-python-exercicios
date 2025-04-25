# Verifique se um número é perfeito (a soma dos seus divisores, excluindo ele mesmo, é igual a ele).

n = int(input("Digite um número: "))
soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print(n, "é um número perfeito.")
else:
    print(n, "não é um número perfeito.")