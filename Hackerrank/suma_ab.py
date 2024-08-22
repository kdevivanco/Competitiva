def sumab():
    it = input('Number of iterations:')
    results = []
    for i in it: 
        n = input("Number:")
        n_s = str(n)
        a = int(n_s[0])
        b = int(n_s[1])
        results.append(a+b)
    for r in results:
        print(r)
        



sumab()
