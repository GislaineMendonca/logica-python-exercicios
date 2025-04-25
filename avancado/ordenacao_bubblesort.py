#Implemente um algoritmo de ordenação sem usar funções prontas do Python.

def bubble_sort(lista):
    n = len(lista)
    # Percorre todos os elementos
    for i in range(n):
        # Últimos i elementos já estão no lugar
        for j in range(0, n-i-1):
            # Troca se o elemento encontrado for maior que o próximo
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)