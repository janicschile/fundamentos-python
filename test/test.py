
def divisible(maximo):
    array = [] # array Final
    arrayTransito = [] # array de consulta

    for x in range(1, maximo + 1 , 1):
        array.append(x)
        arrayTransito.append(x)
    array.remove(1) # eliminamos 1 que no es considerado primo de array Final
    arrayTransito.remove(1) # eliminamos 1 que no es considerado primo de array Transito

    print("Largo de Array Final:" , len(array))
    for i in range(0, len(arrayTransito)):
        # print("NO CUMPLE: bucle" , i , "Dato a revisar: " , arrayTransito[i], "- Largo de arrayTransito", len(arrayTransito), "- Largo de array", len(array))
        if ((arrayTransito[i])/2).is_integer():
            # print("SI CUMPLE: Valor divisible a eliminar: " , arrayTransito[i])
            if arrayTransito[i] in array:
                array.remove(arrayTransito[i]) # eliminamos multiplos de 2 que no es considerado primo
                print(array)
                continue

    print("Largo de Array Final 2:" , len(array))
    for i in range(0, len(arrayTransito)):
        print("NO CUMPLE: bucle" , i , "Dato a revisar: " , arrayTransito[i], "- Largo de arrayTransito", len(arrayTransito), "- Largo de array", len(array))
        if ((arrayTransito[i])/5).is_integer():
            print("SI CUMPLE: Valor divisible a eliminar: " , arrayTransito[i])
            if arrayTransito[i] in array:
                array.remove(arrayTransito[i]) # eliminamos multiplos de 2 que no es considerado primo
                print(array)
                continue

    
    newMaxArray = len(array)
    print(newMaxArray)

    print(array)
    print(len(array))
    
cantMax = 100
print(divisible(cantMax))

