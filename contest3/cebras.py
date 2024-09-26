def count_bells(creatures):
    cola = creatures
    veces = 0

    while True:
        index = -1
        for i in range(len(cola) - 1, -1, -1):
            if cola[i] == 'O':
                index = i
                break
        
        if index == -1:
            break

        # Incrementa veces por la cantidad de posiciones hasta el ocelote
        veces += (index + 1)
        # Cambia el ocelote más bajo a cebra
        cola[index] = 'Z'

        # Convierte todas las cebras debajo en ocelotes
        for i in range(index - 1, -1, -1):
            if cola[i] == 'Z':
                cola[i] = 'O'
    
    veces -= 1
    return veces

# Leer entrada
N = int(input())
creatures = [input().strip() for _ in range(N)]

# Calcular y mostrar el resultado
print(count_bells(creatures))
