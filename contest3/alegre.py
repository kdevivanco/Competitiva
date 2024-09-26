# Una secuencia de n > 0 n>0 enteros se llama un saltador alegre si los valores absolutos de la diferencia entre elementos sucesivos toman todos los valores de 1 1 a través de n − 1 n−1. 
# Por ejemplo, 1 4 2 3 es un saltador alegre, porque las diferencias absolutas son 3 3, 2 2, y 1 1 respectivamente.
#  La definición implica que cualquier secuencia de un solo entero es un saltador alegre. Debes escribir un programa para determinar 
# si cada una de una serie de secuencias es un saltador alegre o no. Entrada Cada línea de entrada contiene un entero n ≤ 3000 n≤3000 seguido de n n enteros que representan la secuencia. Los valores en la secuencia son como máximo 300 000 300000 en valor absoluto. 
# La entrada contiene como máximo 10 10 líneas.

# 4 1 4 2 3
# 5 1 4 2 -1 6
# 

# import pdb

def saltador(a):
    n = int(a[0])
    a = a[1:]
    a = [int(i) for i in a]
    
    # Si n es 1, automáticamente es alegre
    if n == 1:
        print("Jolly")
        return

    # Calculamos las diferencias absolutas
    abs_dif = set(abs(a[i] - a[i + 1]) for i in range(n - 1))

    # Comprobamos si las diferencias contienen todos los números de 1 a n-1
    if abs_dif == set(range(1, n)):
        print("Jolly")
    else:
        print("Not jolly")

def main():
    try:
        while True:
            a = input().split()
            if not a:  # Si no hay entrada, salimos
                break
            saltador(a)
    except EOFError:
        return

main()


# def saltador(a):
#     # print(a)
#     # pdb.set_trace()
#     n = int(a[0])
#     a = a[1:]
#     a = [int(i) for i in a]

#     abs_dif = []

#     for i in range(n-1):
#         abs_dif.append(abs(a[i]-a[i+1]))


#     m =len(abs_dif)
#     jolly = True
#     for i in range(m-1):
#         if abs_dif[i] - abs_dif[i+1] != 1: 
#             jolly = False
#             break
        
#     if jolly == True: 
#         print("Alegre")
#     else: 
#         print("No alegre")

# def main():
#     for i in range(10):
#         a = list(input().split())
#         if len(a) == 0:
#             return
#         saltador(a)

# main()