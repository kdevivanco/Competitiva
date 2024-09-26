# Un cuadrado de área positiva (estrictamente mayor que 0)
# se encuentra en el plano de coordenadas, con lados paralelos a los ejes de coordenadas.
# Se te dan las coordenadas de sus esquinas, en orden aleatorio.
# Tu tarea es encontrar el área del cuadrado.

test_cases = input()

for i in range(int(test_cases)):
    coord1 = input()
    coord2 = input()
    coord3 = input()
    coord4 = input()
    x1, y1 = map(int, coord1.split(' '))
    x2, y2 = map(int, coord2.split(' '))
    x3, y3 = map(int, coord3.split(' '))
    x4, y4 = map(int, coord4.split(' '))


    array_x_coords = [x1, x2, x3,x4]
    array_y_coords = [y1, y2, y3,y4]
    array_x_coords.sort()
    array_y_coords.sort()

    x_dist = array_x_coords[3] - array_x_coords[0]
    y_dist = array_y_coords[3] - array_y_coords[0]

    area = x_dist * y_dist

    print(area)


