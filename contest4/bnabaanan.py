# n,k = map(int, input().split(" "))

# fibibib = [0,1,1]
# for i in range(n+1):
#     fib.append(fib[-1] + fib[-2])

# while n > 2:
#     if k > fib[n-2]:
#         k -= fib[n-2]
#         n -= 1
#     else:
#         n -= 2

# if n == 1:
#     print("N")

# if n == 2:
#     print("A")

def banana(n,k):
    fibibib = [0,1,1] #iniciamos a fibonaci
    for i in range(n+1):
        fibibib.append(fibibib[-1] + fibibib[-2]) #apend cada valor

    while n > 2: 
        if k > fibibib[n-2]:
            k -= fibibib[n-2]
            n -= 1
        else:
            n -= 2

    if n == 1:
        return "N"
    if n == 2:
        return "A"
    
n,k = map(int, input().split(" "))
print(banana(n,k))