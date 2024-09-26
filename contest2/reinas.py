def check(tablero, fila, col, columnas, diag1, diag2):
    safe =  columnas[col] == diag1[fila + col] == diag2[fila - col + 7] == False
    return safe

def tablerores(tablero, fila, columnas, diag1, diag2):
    if fila == 8:
        return 1  #solu valida

    total = 0

    for col in range(8):
        if tablero[fila][col] == '.' and check(tablero, fila, col, columnas, diag1, diag2):
            # marca
            columnas[col] = diag1[fila + col] = diag2[fila - col + 7] = True

            # recurse
            total += tablerores(tablero, fila + 1, columnas, diag1, diag2)

            # backtrack
            columnas[col] = diag1[fila + col] = diag2[fila - col + 7] = False

    return total

def countways(tablero):
    columnas = [False] * 8
    diag1 = [False] * 15
    diag2 = [False] * 15
    return tablerores(tablero, 0, columnas, diag1, diag2)

tablero = [input().strip() for _ in range(8)]

print(countways(tablero))
