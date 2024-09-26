
# Input: 
# 4 1 25 2 3
# 4 1 2 2 3
# 8 90 4 10000 2 18 60 172 99
# 0

# Output: 
# 3 1 2 3
# 3 1 2 3
# 4 2 18 60 99


import pdb
# def longest_increasing_subsequence(n, a):
#     dp = [1] * n
    
#     for i in range(n):
#         for j in range(i):
#             if a[j] < a[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)
    
#     subsequence = get_subsequence(a,dp)
#     # print(max(dp))
#     string_subsequence = ''
#     for elem in subsequence:
#         string_subsequence += str(elem) + ' '
#     string_subsequence = string_subsequence[:-1]
#     print(f'{max(dp)} {string_subsequence}')
    # print_subsequence(a,dp)

    

# old implementation::::: 

# def get_subsequence(a,dp):
#     n = len(a)
#     print(dp)
#     max_length = max(dp)
#     print(f'max length: {max_length}')
#     index = dp.index(max_length)
#     sequence = [a[index]]
#     for i in range(index-1,-1,-1):
#         if dp[index] == dp[i] + 1:
#             sequence.append(a[i])
#             index = i
#     return(sequence[::-1])


def get_subsequence(a, dp):
    n = len(a)
    max_length = max(dp)
    index = dp.index(max_length)
    
    elemnt = [i for i in range(n) if dp[i] == max_length]


    index = elemnt[0]
    for i in elemnt:
        if a[i] < a[index]:
            index = i

    sequence = [a[index]]
    max_length -= 1
    
    for i in range(index - 1, -1, -1):
        if dp[i] == max_length and a[i] < a[index]:
            sequence.append(a[i])
            index = i
            max_length -= 1
    
    return sequence[::-1]


def longest_increasing_subsequence(n, a):
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    subsequence = get_subsequence(a, dp)
    string_subsequence = ' '.join(map(str, subsequence))
    print(f'{max(dp)} {string_subsequence} ')



# Leer input separado por \n: 
# Ejemplo de input: 
#4 1 25 2 3
# 4 1 2 2 3
# 8 90 4 10000 2 18 60 172 99
# 0




# n, *a = map(int, input().split())

# longest_increasing_subsequence(n, a)

while True:
    entrada = input().strip()
    
    numeros = list(map(int, entrada.split()))
    
    if numeros[0] == 0:
        break
    
    n = numeros[0]
    a = numeros[1:]
    
    longest_increasing_subsequence(n, a)


# # Leer input
# n, *a = map(int, input().split())

# # Llamada a la función principal
# longest_increasing_subsequence(n, a)

