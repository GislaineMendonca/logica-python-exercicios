# Implemente um algoritmo de ordenação sem usar funções prontas do Python.

def quicksort(lista):
    # Função auxiliar para executar o quicksort recursivamente
    def _quicksort(lista, inicio, fim):
        if inicio < fim:
            # Particiona a lista e obtém o índice do pivô
            pivo_idx = particionar(lista, inicio, fim)
            
            # Ordena recursivamente os elementos antes e depois do pivô
            _quicksort(lista, inicio, pivo_idx - 1)
            _quicksort(lista, pivo_idx + 1, fim)
    
    # Inicia o quicksort
    _quicksort(lista, 0, len(lista) - 1)
    return lista

def particionar(lista, inicio, fim):
    # Escolhe o último elemento como pivô
    pivo = lista[fim]
    i = inicio  # Índice do menor elemento
    
    for j in range(inicio, fim):
        # Se o elemento atual é menor ou igual ao pivô
        if lista[j] <= pivo:
            # Troca os elementos
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    
    # Coloca o pivô na posição correta
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

# Exemplo de uso
lista = [22, 7, 10, 9, 3, 5]
print("Lista original:", lista)
lista_ordenada = quicksort(lista)
print("Lista ordenada:", lista_ordenada)