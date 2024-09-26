
import pdb
def find_constant(n, t, segments):
    low, high = -1000000000, 1000000000 
    
    def time_for_c(c):
        total_time = 0
        for d, s in segments:
            if s + c <= 0: 
                return float('inf')  
            total_time += d/(s+c)
        return total_time
    
    while high - low > 1e-10:  
        mid = (low + high) / 2
        if time_for_c(mid) > t:  #c muy pequeno
            low = mid
        else:
            high = mid
    
    
    return mid, t, segments 

n, t = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(n)]

c, time, seg = find_constant(n, t, segments)
# print(f"{result:.9f}")


for i in range (len(seg)):
    distance_traveled = (seg[i][1]+c) * seg[i][0]
    print(f'distance traveled: {distance_traveled}')

