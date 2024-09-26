# Se te da un tetraedro. Vamos a marcar sus vértices con las letras A, B, C y D respectivamente. 
# Una hormiga está de pie en el vértice D del tetraedro. 
# La hormiga es bastante activa y no se quedará quieta. 
# 
# En cada momento de tiempo, da un paso de un vértice a otro a lo largo de alguna arista del tetraedro. 
# La hormiga simplemente no puede quedarse en un solo lugar. No tienes que hacer mucho para resolver el problema:
#  tu tarea es contar el número de formas en que la hormiga puede ir desde el vértice inicial D a sí misma en exactamente n pasos. 
# En otras palabras, se te pide que encuentres el número de diferentes caminos cíclicos con una longitud de n desde el vértice D hasta sí mismo.
#  Como el número puede ser bastante grande, debes imprimirlo módulo 1000000007 (10^9 + 7).

# // input : La primera línea contiene el único entero n (1 ≤ n ≤ 107) — la longitud requerida del camino cíclico.

#Output: Imprime el único entero — el número requerido de formas módulo 1000000007 (10^9 + 7).




MOD = 1000000007

def matrix(i,j):
    return [ [(i[0][0] * j[0][0] + i[0][1] * j[1][0]) % MOD,
              (i[0][0] * j[0][1] + i[0][1] * j[1][1]) % MOD],
              [(i[1][0] * j[0][0] + i[1][1] * j[1][0]) % MOD, 
               (i[1][0] * j[0][1] + i[1][1] * j[1][1]) % MOD]
            ]


def pow(a, n):
    result = [[1, 0], [0, 1]]
    base = a
    
    while n > 0:
        if n % 2 == 1:
            result = matrix(result, base)
        base = matrix(base, base)
        n //= 2
    
    return result


def hormiga(n):
    if n == 0:
        return 1
    
    a = [[0, 3],
         [1, 2]]
    
    an = pow(a, n)
    
    dcero = 1
    xcero = 0
    dpD_n = (an[0][0] * dcero + an[0][1] * xcero) % MOD
    
    return dpD_n

n = int(input())
print(hormiga(n))