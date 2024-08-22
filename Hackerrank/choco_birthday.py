def birthday(s, d, m):
    suma = 0
    segment = 0
    ways = 0
    if len(s) == 1: 
        if s[0] == d: 
            return 1
        else: 
            return 0
    for i in s: 
        segment += 1
        while segment <= m: 
            suma += i
            if suma == d :
                print (suma)
                ways += 1
                suma = 0
                segment = 0
                continue
            else: 
                break
                
    return ways 



s = [4] 
d= 4
m = 1

print(birthday(s,d,m))