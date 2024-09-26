

n = int(input())
values = input()
values = values.split()
values = [int(i) for i in values]

def moneditas(values):
    values.sort()
    for i in range(1, len(values)):
        if values[i] % values[0] != 0:
            return "non-canonical"
    return "canonical"


print(moneditas(values))