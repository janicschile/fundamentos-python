# coding=utf-8

# 1. TAREA: imprimir "Hola mundo"
print("Hola Mundo")


# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Oscar"
print( "hola", name)	# con una coma  //res: 
print( "hola " + name)	# con un +      //res: 



# 3. imprimir "Hola 42!" con un numero en una variable
name = 17
print("hola" , name)	# con una coma                                      //res: hola 17
# print("hola" + name)	# con una coma                                      //res: TypeError: can only concatenate str (not "int") to str


#NINJA BONUS
name = 17
print("hola " + str(name) )	# con un + - !Este debería darnos un error!     //res: res: hola 17


# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "pizza"
fave_food2 = "hamburguesas"
print("Me encanta comer {} y {}.".format(fave_food1, fave_food2)) # con .format()
print(f"Me encanta comer {fave_food1} y {fave_food2}.") # con una cadena f


#NINJA BONUS
print("enero\tfebrero\tmarzo")  # Tabulaciones 