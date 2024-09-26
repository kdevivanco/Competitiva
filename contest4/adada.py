# Por motivo de cumpleaños de Luis, y como celebración de que todos aprobaron ADA, 
# este problema solo te pide calcular eficientemente los valores a^b modulo 10^9 + 7
# Solo porque hoy es viernes 13, asumiremos que  0^0 = 1

# Entrada:
# La primera línea de entrada contiene un entero  n: el número de cálculos. 
# Después de esto, hay nn líneas, cada una conteniendo dos enteros a y b

# Salida:
# Imprime cada valor  a^b modulo 10^9 + 7

# Restricciones:
# 1≤n≤2*10^5
# 0≤a,b≤10 

# def cumpleluis():
#     n = int(input())
#     for _ in range(n):
#         a, b = map(int, input().split())
#         if a == 0 and b == 0:
#             print(1)
#         else:
#             print(pow(a, b, 10**9+7))


# cumpleluis()

MOD = 1000000007

def cumplele(a,b):
    if b == 0:
        return 1
    x = cumplele(a, b // 2)
    if b % 2 == 0:
        return x * x % MOD
    return x * x * a % MOD

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(cumplele(a, b))


