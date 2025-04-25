# Escreva uma função que inverta uma string sem usar funções prontas do Python.

s = input("Digite uma string: ")
invertida = ""
i = len(s) - 1

while i >= 0:
    invertida += s[i]
    i -= 1

print("String invertida:", invertida)