# La primera línea de la entrada contiene el número de casos de prueba T T. 
# Las descripciones de los casos de prueba siguen: La primera línea de cada caso de prueba 
# contiene la grabación—palabras sobre el alfabeto inglés en minúsculas, separadas por espacios. 
# Cada una contiene como máximo 100 letras y no hay más de 100 palabras. 
# Las siguientes líneas son tu información pre-recolectada sobre otros animales, 
# en el formato <animal> hace <sonido>. No hay más de 100 animales, sus nombres no son más 
# largos de 100 letras cada uno y son nombres reales de animales en inglés. No hay el zorro hace ... 
# entre estas líneas. La última línea del caso de prueba es exactamente 
# la pregunta que se supone que debes responder: ¿qué dice el zorro?



def fox():
    code_string = str(input())
    # print(code_string)
    #split code_string :
    code_string = code_string.split()
    # print(code_string)
    animal_sounds =[]
    while True:
        animal_string = str(input())
        if animal_string == 'what does the fox say?':
            break
        #split on spaces:
        animal_string = animal_string.split()
        animal_sounds.append(animal_string[2])
    
    the_fox_says = ''
    for word in code_string: 
        if word in animal_sounds:
            continue
        else: 
            the_fox_says = the_fox_says + word + ' '
    print(the_fox_says[:-1])
    

n = int(input())
for i in range(n):
    fox()

