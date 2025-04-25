# Verifique se uma grade 9x9 de Sudoku está corretamente preenchida.

def verificar_sudoku(sudoku):
    # Verificar se todas as linhas são válidas
    for linha in sudoku:
        if len(set(linha)) != 9 or any(x < 1 or x > 9 for x in linha):
            return False
    
    # Verificar se todas as colunas são válidas
    for col in range(9):
        coluna = [sudoku[linha][col] for linha in range(9)]
        if len(set(coluna)) != 9:
            return False

    # Verificar se todas as subgrades 3x3 são válidas
    for i in range(3):
        for j in range(3):
            subgrade = [sudoku[x][y] for x in range(i*3, (i+1)*3) for y in range(j*3, (j+1)*3)]
            if len(set(subgrade)) != 9:
                return False

    return True

# Exemplo de Sudoku válido (9x9)
sudoku_exemplo = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Exemplo de Sudoku inválido (9x9)
sudoku_exemplo2 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 7, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 1, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 8, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Verificar se o Sudoku está correto
if verificar_sudoku(sudoku_exemplo):
    print("Sudoku válido!")
else:
    print("Sudoku inválido!")
