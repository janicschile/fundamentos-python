import time
import os
import ast

# Base Datos Inicial (pasar a archivo escribible)
#bdUsuarios = [
#     {'username':'oguerrero', 'password':'1234', 'nombre':'Oscar', 'apellido' : 'Guerrero', 'email' : 'oguerrerog@gmail.com', 'balance' : 0},
#     {'username':'mjackson', 'password':'1234', 'nombre':'Michael', 'apellido' : 'Jackson', 'email' : 'jackson@gmail.com', 'balance' : 100000}
#]

def leerArchivoClientes():
    #bdUsuarios = []
    bd = open("bdusuarios.txt", "r")
    raw_data = bd.read()  #.split('\n')
    bdUsuarios = ast.literal_eval(raw_data)
    bd.close()
    return bdUsuarios

def guardarArchivoClientes(bdUsuarios):
    bd = open("bdusuarios.txt", "w")
    bd.write(str(bdUsuarios))
    bd.close()
    return ""


class User:		# Datos cargados del usuario LOGIN cajero
    def __init__(self, username, password, nombre, apellido, email, balance):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.balance = float(balance)

    # agrega el método Depositar 
    def deposito(self, deposito):	# toma un argumento que es el monto del depósito
        self.balance += deposito	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        for i in bdUsuarios:
            if i["username"] == dataCliente.username:
                i["balance"] = dataCliente.balance
    
    # agrega el método Retiro 
    def retiro(self, retiro):	# toma un argumento que es el monto del depósito
        self.balance -= retiro	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        for i in bdUsuarios:
            if i["username"] == dataCliente.username:
                i["balance"] = dataCliente.balance

def screen_clear():
    if os.name == 'posix':  # Linux y MAC
        _ = os.system('clear')
    else:
        _ = os.system('cls') # Windows

def titulo():
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓╔═════════════════════════════════╗▓▓▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓║       CAJERO PYTHON 1.0         ║░░▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓╚═════════════════════════════════╝░░▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")



def cajeroOnline():
    screen_clear()
    titulo()
    creaCuenta = int(input("\n Opcion 1: Ingreso Clientes\n Opcion 2: Crear Cuenta\n Seleccionar Opcion (1/2): "))
    if creaCuenta == 1:
        return ""

    if creaCuenta == 2:
        # paso 1
        screen_clear(); titulo();
        creaUsuario  = input("\n Ingrese su Nombre de Usuario : ")
        creaPassword = input(" Ingrese su Contraseña        : ")
        creaNombre   = input(" Ingrese su Nombre            : ")
        creaApellido = input(" Ingrese su Apellido          : ")
        creaEmail    = input(" Ingrese su Email             : ")
        
        screen_clear(); titulo();
        print(f"\n Los datos ingresados son:\n\n Nombre Usuario: {creaUsuario}\n Contraseña: {creaPassword}\n Nombre Completo: {creaNombre} {creaApellido}\n Email: {creaEmail}")
        creaCliente = input("\n ¿Esta seguro de crear su cuenta en Banco Python?\n Seleccionar Opcion (s/n): ")
        if creaCliente == "s" or  creaCliente == "S":
            transito = [{'username': creaUsuario, 'password': creaPassword, 'nombre': creaNombre, 'apellido' : creaApellido, 'email' : creaEmail, 'balance' : 0}]
            bdUsuarios = leerArchivoClientes()
            bdUsuarios.append(transito)
            guardarArchivoClientes(bdUsuarios)
            cajeroOnline()

        if creaCliente == "n" or creaCliente == "N":
            cajeroOnline()

        if creaCliente != "s" and creaCliente != "S" and creaCliente != "n" and creaCliente != "N":
            print("\n ---> Seleccion no valida...")
            time.sleep(2)
            cajeroOnline()

    if creaCuenta != 1 and creaCuenta != 2:
        print("\n ---> Seleccion no valida...")
        time.sleep(2)
        cajeroOnline()
    
    

def login(username, bdUsuarios):
    cliente = ""
    screen_clear() #╚ ╔ ╗╝ ║ ╩ ╦
    titulo()

    dato = input("\nIngrese su Nombre de Usuario: ")
    for cliente in bdUsuarios:
        if cliente[username] == dato:
            return cliente 
    screen_clear()
    titulo()
    print("\nEl cliente ingresado, no existe en nuestros registros...")
    time.sleep(3)
    screen_clear()
    dato;
    cliente;
    return login('username', bdUsuarios)

def opcionUno():
    screen_clear()
    print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║    CONSULTA  DE  SALDO   ║\n           ╚══════════════════════════╝\n")
    print(f"Estimado {dataCliente.nombre.title()} {dataCliente.apellido.title()}, su saldo disponible es de ${dataCliente.balance} ..\n\n\n")
    os.system("Pause")
    return menuSistema()

def opcionDos():
    screen_clear()
    print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║      GIRO  DE  DINERO    ║\n           ╚══════════════════════════╝\n")
    print(f"- Saldo disponible en su Cuenta ${dataCliente.balance} ..\n\n")
    while True:
        try:
            retiro = int(input("\nINGRESE EL MONTO A RETIRAR (ingrese 0 para volver): "))
            break
        except:
            opcionDos()
    if dataCliente.balance < retiro or dataCliente.balance < 1 or dataCliente.balance == "":
        screen_clear()
        print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║      GIRO  DE  DINERO    ║\n           ╚══════════════════════════╝\n")
        print(f"- Saldo insuficiente en su Cuenta para realizar retiro.\nSALDO DISPONIBLE: ${dataCliente.balance}.-\n\n")
        os.system("Pause")
        return menuSistema()
    else:
        screen_clear()
        dataCliente.retiro(retiro)
        print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║      GIRO  DE  DINERO    ║\n           ╚══════════════════════════╝\n")
        print(f"- Usted ha retirado ${retiro}.- de su cuenta.\nNUEVO SALDO DISPONIBLE: ${dataCliente.balance}.-\n\n")
        os.system("Pause")
        return menuSistema()

def opcionTres():
    screen_clear()
    print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║   DEPOSITO  DE  DINERO   ║\n           ╚══════════════════════════╝\n")
    print(f"- Saldo disponible en su Cuenta ${dataCliente.balance} ..\n\n")
    deposito = int(input("\nINGRESE EL MONTO A DEPOSITAR: "))
    if deposito <= 1000:
        screen_clear()
        print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║   DEPOSITO  DE  DINERO   ║\n           ╚══════════════════════════╝\n")
        print(f"- El monto minimo para deposito es de $1.000.-\nSALDO DISPONIBLE: ${dataCliente.balance}.-\n\n")
        os.system("Pause")
        return menuSistema()
    else:
        screen_clear()
        dataCliente.deposito(deposito)
        print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║   DEPOSITO  DE  DINERO   ║\n           ╚══════════════════════════╝\n")
        print(f"- Usted ha depositado correctamente ${deposito}.- en su cuenta.\nNUEVO SALDO DISPONIBLE: ${dataCliente.balance}.-\n\n")
        os.system("Pause")
        return menuSistema()

def opcionCuatro():
    screen_clear()
    print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║    CONSULTA  DE  SALDO   ║\n           ╚══════════════════════════╝\n")
    print(f"Estimado {dataCliente.nombre.title()} {dataCliente.apellido.title()}\nsu saldo disponible es de ${dataCliente.balance} ..\n\n\n")
    os.system("Pause")
    return menuSistema()
def menuSistema():
    screen_clear()    #╚ ╔ ╗╝ ║ ╩ ╦
    print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║     MENU   PRINCIPAL     ║\n           ╚══════════════════════════╝\n")
    print(f"         BIENVENIDO: {dataCliente.nombre.upper()} {dataCliente.apellido.upper()}\n")
    print("1 >> Consulta de Saldo                Giro de Dinero << 2")
    print("3 >> Depositos                        Transferencias << 4")
    print("5 >> Mis Datos                                 SALIR << 6")
    opcion = int(input("\n             Ingrese Opcion: "))
    print(opcion)

    if opcion == 1 : opcionUno()

    if opcion == 2: opcionDos()

    if opcion == 3 : opcionTres()
    
    if opcion == 4 : 
        print("\n Opcion aun sin implementar, favor de utilizar plataforma Web..."); time.sleep(3); return menuSistema()

    if opcion == 5 :
        screen_clear()
        print("\n                CAJERO PYTHON 1.0\n        ═══╦══════════════════════════╦═══\n           ║    DATOS  DEL  CLIENTE   ║\n           ╚══════════════════════════╝\n")
        print(f"Nombre del Cliente : {dataCliente.nombre.title()} {dataCliente.apellido.title()}")
        print(f"Correo Electronico : {dataCliente.email}")
        print(f"Saldo Contable     : ${dataCliente.balance}.-")
        print("\n")
        os.system("Pause")
        return menuSistema()

    if opcion == 6 :
        screen_clear()
        #print(bdUsuarios)
        #print(dataCliente.balance)
        guardarArchivoClientes(bdUsuarios)
        #os.system("Pause")



    if opcion == 00:
        guido = User("Guido van Rossum", "guido@python.com")
        monty = User("Monty Python", "monty@python.com")
        print(guido.nombre)	# salida: Guido van Rossum
        print(monty.nombre)	# salida: Monty Python
        print(guido.nombre)	# salida: Michael
        print(monty.nombre)	# salida: Michael
        User.deposito(100)

while True:
    leerArchivoClientes()
    cajeroOnline()
    bdUsuarios = leerArchivoClientes()
    loginCorrecto = login('username', bdUsuarios)
    dataCliente = User(loginCorrecto["username"],loginCorrecto["password"],loginCorrecto["nombre"], loginCorrecto["apellido"], loginCorrecto["email"], loginCorrecto["balance"]) 
    #os.system("Pause")
    #time.sleep(3)
    #ejecutar menuSistema
    menuSistema()