# Entrada: 5 caracteres. 
# Todos los caracteres serán ya sea ’k’, indicando la colocación de un caballo, o ’.’, 
# indicando un espacio vacío en el tablero.

def horses():
    #crear matriz 5x5
    line1 = input()
    line1 = [line1[0],line1[1],line1[2],line1[3],line1[4]]
    line2 = input()
    line2 = [line2[0],line2[1],line2[2],line2[3],line2[4]]
    line3 = input()
    line3 = [line3[0],line3[1],line3[2],line3[3],line3[4]]
    line4 = input()
    line4 = [line4[0],line4[1],line4[2],line4[3],line4[4]]
    line5 = input()
    line5 = [line5[0],line5[1],line5[2],line5[3],line5[4]]

    tablero = [line1,line2,line3,line4,line5]
    all_items = [item for sublist in tablero for item in sublist]
    #count all ks in all:
    count = all_items.count('k')
    if count != 9: 
          print ("invalid")
          return

    matches = []
    for i in range(5):
        line = tablero[i]
        for j in range(5):
            
            position = line[j]
            #DERECHA HORIZONTAL ARRIBA:
            if i < 4 and j < 3: #si estamos en cualquiera debajo de la ultima
                    match = tablero[i+1][j+2]
                    matches.append((position,match))
            #DERECHA VERTICAL ARRIBA:
            if i < 3 and j < 4:
                    match = tablero[i+2][j+1]
                    matches.append((position,match))
            #IZQUIERDA HORIZONTAL ARRIBA
            if i < 4 and j > 1:
                    match = tablero[i+1][j-2]
                    matches.append((position,match))
            #IZQUIERDA VERTICAL ARRIBA
            if i < 3 and j > 0:
                    match = tablero[i+2][j-1]
                    matches.append((position,match))
            #DERECHA HORIZONTAL ABAJO:
            if i > 0 and j < 3:
                    match = tablero[i-1][j+2]
                    matches.append((position,match))
            #DERECHA VERTICAL ABAJO: 
            if i > 1 and j < 4:
                    match = tablero[i-2][j+1]
                    matches.append((position,match))
            #IZQUIERDA VERTICAL ABAJO:
            if i > 1 and j > 0:
                    match = tablero[i-2][j-1]
                    matches.append((position,match))
            #IZQUIERDA HORIZONTAL ABAJO:
            if i > 0 and j > 1:
                    match = tablero[i-1][j-2]
                    matches.append((position,match))
            
    #iteramos los matches:
    for match in matches:
        if match[0] == 'k' and match[1] == 'k':
            print("invalid")
            return
    
    print("valid")



horses()