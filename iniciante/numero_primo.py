# Verifique se um número é primo.

numero = int(input("Digite um número: "))

if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")