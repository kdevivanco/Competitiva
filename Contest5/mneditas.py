def dp_vals(amount, valores):
        dp = [float('inf')] * (amount + 1) #dp min min

        dp[0] = 0
        
        for coin in valores:
            for i in range(coin, amount + 1):
                #llamada dpdp

                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp
    
def mini_vals(amount, valores):
        count = 0
        for coin in reversed(valores):
            count += amount // coin
            amount %= coin
        return count
def canonico(n, valores):
    max_val = valores[-1] + valores[-2]
    
    dp = dp_vals(max_val, valores)
    
    for x in range(1, max_val + 1):
        minicount = mini_vals(x, valores)
        if minicount > dp[x]:
            return "non-canonical"
    
    return "canonical"



n = int(input())  
valores = list(map(int, input().split()))  

print(canonico(n, valores))
