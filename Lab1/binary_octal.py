# Escribe un programa que convierta un número binario a octal para que Slavko pueda verificar sus resultados.

def binary_to_octal():
    binary_representation = input()

    str(binary_representation)
    while len(binary_representation) % 3 != 0:
        binary_representation = "0" + binary_representation

   
    octal_representation = ""
    for i in range(0, len(binary_representation), 3):
        octal_representation += str(int(binary_representation[i:i+3], 2))
    
    print(octal_representation)

binary_to_octal()

        


