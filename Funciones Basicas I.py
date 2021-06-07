# Ejercicio #1
def a():
    return 5
print(a())
### Imprime en pantalla: 5
###

# Ejercicio #2
def a():
    return 5
print(a()+a())
### Imprime en pantalla: 10
###


# Ejercicio #3
def a():
    return 5
    return 10
print(a())
### Imprime en pantalla: 5  -->  10 es omitido
###


# Ejercicio #4
def a():
    return 5
    print(10)
print(a())
### Imprime en pantalla: 5 -->  print(10) es omitido
###



# Ejercicio #5
def a():
    print(5)
x = a()
print(x)
### Imprime en pantalla: 5, None  --> None indica que no hay return
###



# Ejercicio #6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
### Imprime en pantalla: 3, 5, None
###
### OBSERVACION: ERROR FATAL 
###



# Ejercicio #7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
### Imprime en pantalla: 25
###



# Ejercicio #8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
### Imprime en pantalla: 100, 10
###



# Ejercicio #9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
### Imprime en pantalla: 7, 14, 21
###



# Ejercicio #10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
### Imprime en pantalla: 8
###



# Ejercicio #11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
### Imprime en pantalla: 500, 500, 300, 500
###



# Ejercicio #12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
### Imprime en pantalla: 500, 500, 300, 500
###



# Ejercicio #13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
### Imprime en pantalla: 500, 500, 300, 300
###

# Ejercicio #14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
### Imprime en pantalla: 1, 2, 3
###

# Ejercicio #15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
### Imprime en pantalla: 1, 3, 5, 10
###
