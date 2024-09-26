# Probablemente hayas oído hablar de la estructura de datos deque (doble cola), 
# que permite insertar y sacar elementos de manera eficiente tanto del frente 
# como de la parte trasera de la cola. Dependiendo de la implementación, 
# también permite un acceso aleatorio eficiente a cualquier índice del elemento de la cola. 
# ¡Ahora, queremos llevar esta estructura de datos al siguiente nivel, la teque (cola triple)! 
# La teque admite las siguientes cuatro operaciones: 
#   push_back x: inserta el elemento x  en la parte trasera de la teque. 
#   push_front x: inserta el elemento x  en el frente de la teque. 
#   push_middle x: inserta el elemento x x en el medio de la teque. 
# El elemento insertado x  ahora se convierte en el nuevo elemento medio de la teque. 
# Si  k es el tamaño de la teque antes de la inserción, el índice de inserción para x es (k+1)/2 
# (usando indexación basada en  0). 
#   get i: imprime el elemento de índice i th (0-basado) de la teque. 
# 
# Entrada:
# 
# La primera línea contiene un entero (1≤N≤10^6 ) 
# que indica el número de operaciones para la teque. 
# Cada una de las siguientes N N líneas contiene una cadena S, 
# que indica uno de los comandos anteriores, seguido de un entero x. 
# Si S es un comando push_back, push_front, o push_middle, x  (1≤x≤10 9 ),
#  de lo contrario, para un comando get, i i ( 0 ≤ i ≤ ( size of teque ) − 1 0≤i≤(size of teque)−1). 
# 
# Garantizamos que la teque no está vacía cuando se da algún comando get. Salida Para cada comando get i, 
# imprime el valor dentro del elemento de índice i th i th de la teque en una nueva línea. Advertencia Los archivos de E/S son grandes. Por favor, utiliza métodos de E/S rápidos.


# def teque():
#     operations = int(input())
#     teque = []
#     for _ in range(operations):
#         command, value = input().split()
#         value = int(value)
#         if command == "push_back":
#             teque.append(value)
#         elif command == "push_front":
#             teque.insert(0, value)
#         elif command == 'get':
#             print(teque[value])
#         elif command == "push_middle":
#             teque.insert((len(teque) + 1) // 2, value)

# teque()


from collections import deque

def teque():
    operations = int(input())
    front = deque()
    back = deque()
    
    for _ in range(operations):
        command, value = input().split()
        value = int(value)
        
        if command == "push_back":
            back.append(value)
        elif command == "push_front":
            front.appendleft(value)
        elif command == "push_middle":
            if len(front) < len(back):
                front.append(value)
            else:
                back.appendleft(value)
        elif command == 'get':
            if value < len(front):
                print(front[value])
            else:
                print(back[value - len(front)])
        
        # Balance the two deques to keep them roughly equal in size
        if len(front) > len(back) + 1:
            back.appendleft(front.pop())
        elif len(back) > len(front):
            front.append(back.popleft())

teque()
