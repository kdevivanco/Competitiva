
# Luis tiene un arreglo a de longitud n que contiene enteros  [k,k+1,...,k+n−1] en ese orden. 
# Luis quiere elegir un índice i (1≤i≤n) de manera que x = abs(a1 ​+a2 ​ +...+ai ​ - ai+1 ​ ...−an ​) se minimice. 
# # Tenga en cuenta que para un entero arbitrario z, abs(z) representa el valor absoluto de z

def calccot(n,k):
    lili =[]
    for i in range(n):
        lili.append(k+i)

    minimo = float('inf')
    indice = 0
    # print(f'elements: {(n+k)/2}')
    # print(f'max: {n-1+k}')

    array_izquierdo = 0
    #copy lili into array derecho:
    array_derecho = []
    array_derecho = [x for x in lili]

    for i in range(n-1):
        array_izquierdo += lili[i]
        array_derecho.pop(0)
        valor_derecho = sum(array_derecho)
        x = abs(array_izquierdo - valor_derecho)
        if x < minimo:
            minimo = x
            indice = i

    print(minimo)
    

n = int(input())
for i in range(n):
    n, k = map(int, input().split())
    calccot(n,k)







# def divide_and_conquer(lili, izq, der):
#     if izq == der:
#         return izq
    
#     mid = (izq + der) // 2
#     suma_izq = sum(lili[:mid + 1])
#     suma_der = sum(lili[mid + 1:])
#     balance = abs(suma_izq - suma_der)
    
#     # Si la mitad actual minimiza la diferencia, la retornamos.
#     if balance == 0:
#         return mid
    
#     # Si no, continuamos buscando en la mitad que podría mejorar la diferencia
#     if suma_izq > suma_der:
#         return divide_and_conquer(lili, izq, mid)
#     else:
#         return divide_and_conquer(lili, mid + 1, der)

# def calccot(n, k):
#     lili = [k + i for i in range(n)]
#     indice = divide_and_conquer(lili, 0, n - 1)
#     x = abs(sum(lili[:indice])-sum(lili[indice:]))
#     print(x)
    

# # Input del problema
# n = int(input())
# for _ in range(n):
#     n, k = map(int, input().split())
#     calccot(n, k)
