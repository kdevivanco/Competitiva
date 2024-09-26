def solve(A, B, C):
    for x in range(-100, 101):
        for y in range(-100, 101):
            z = A - x - y
            if z == x or z == y:
                continue
            if x * y * z == B and x**2 + y**2 + z**2 == C:
                return tuple(sorted([x, y, z]))
    return 'No solution.'

def main():
    N = int(input())
    for _ in range(N):
        A, B, C = map(int, input().split())
        result = solve(A, B, C)
        if result == 'No solution.':
            print(result)
        else:
            print(*result)

if __name__ == '__main__':
    main()
