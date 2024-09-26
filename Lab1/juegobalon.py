

def juego_balon():
    registros = input()
    #Cada registro tiene la sgte estrcutra: H 2 0:13
    registros_formateados = []

    for i in registros: 
        registro = input()
        registro = registro.split(" ")
        tiempo = registro[2].split(":")
        minutos = int(tiempo[0])
        segundos = int(tiempo[1])

        registro = [registro[0], registro[1], minutos,segundos]
    print(registros_formateados)

    
juego_balon()