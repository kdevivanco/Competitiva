# Para dos enteros dados n y k encuentra (Zn +Zn-1 - 2Zn-2)mod 10000007
# donde Zn = Sn + Pn y 
# Sn = 1^k + 2^k + 3^k + ....+ n^k
# y Pn = 1^1 + 2^2 + 3^3 + ....+ n^n

# Entrada: n k

# salida: Valor solicitado


def sumanana(n,k):
    MOD = 10000007
    Zn = []
    Sn = 0
    Pn = 0
    for i in range(1,n+1):
        Sn += pow(i,k)
        # print(i, k ,Sn)
        Pn += pow(i,i)
        # print(i,i,Pn)
        Zn.append(Sn+Pn)
    
    # print(Zn)
    resp = (Zn[-1] + Zn[-2] - 2*Zn[-3])% MOD
    print(resp)


while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    sumanana(n,k)
