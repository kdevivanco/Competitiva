

test_cases = input()
for i in range(int(test_cases)):
    operation = input()
    if operation == "P=NP":
        print("skipped")
    else:
        #separar los numerso antes y dps del +
        operation = operation.split("+")
        #sumar
        print(int(operation[0]) + int(operation[1]))
