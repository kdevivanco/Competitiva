# Tu tarea será escribir un programa para invertir números en binario.
#  Por ejemplo, la representación binaria de 13 es 1101, y al invertirla se obtiene 1011, que corresponde al número 11.


num = int(input())
def decimalToBinary(num): 
    return bin(num).replace("0b", "") 

binnnnn = str(decimalToBinary(num))
inverted = binnnnn[::-1]
decimal = int(inverted, 2)
print(decimal)