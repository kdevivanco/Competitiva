# Por ejemplo, si A’ = { 2 , 1 , 3 , 4 , 7 , 5 , 6 , 8 } {2,1,3,4,7,5,6,8}, 
# entonces 3 enteros: { 3 , 4 , 8 } {3,4,8} podrían haber sido el pivot de la partición, por ejemplo, 
# { 2 , 1 , 3 } {2,1,3} a la izquierda del entero 4 4 son menores que 4 4 y { 7 , 5 , 6 , 8 } {7,5,6,8} a 
# la derecha del entero 4 4 son mayores que 4 4. Sin embargo, los otros 5 enteros no pueden ser el pivot
# , por ejemplo, el entero 7 7 no puede ser el pivot ya que hay { 5 , 6 } {5,6} a la derecha del entero 7 7

# def pivot():
#     n= int(input())
#     A = [int(x) for x in input().split()]
#     pivots= []
    
#     B = []
#     B = [x for x in A]
#     B.sort()
#     if A == B:
#         print(2)
#         return

#     for i in range(len(A)-1):
#         possible_pivot = A[i]

#         left = [x for x in A[:i] if x < possible_pivot]
#         if len(left) < len(A[:i]):
#             continue

#         # print(left)
#         right = [x for x in A[i+1:] if x > possible_pivot]
#         if len(right) < len(A[i+1:]):
#             continue
#         # print(right)
#         if len(left) + len(right) == n - 1:
#             # print("hollaaa")
#             pivots.append(possible_pivot)
#     maximum = max(A)
#     # print(maximum)
#     # print(A[-1])
#     if A[-1] == maximum:
#         pivots.append(maximum)
    
#     # print(pivots)

#     print(len(pivots) )

# pivot()
    

   


def pivot():
    n = int(input())
    A = [int(x) for x in input().split()]
    
    if n == 0:
        print(0)
        return
    
    left_max = [0] * n
    left_max[0] = float('-inf')
    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], A[i-1])
    
    right_min = [0] * n
    right_min[-1] = float('inf')
    
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], A[i+1])
    
    pivot_count = 0
    
    for i in range(n):
        if left_max[i] < A[i] < right_min[i]:
            pivot_count += 1
    
    print(pivot_count)

pivot()
