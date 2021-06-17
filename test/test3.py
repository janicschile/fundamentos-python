
bdUsuarios = [
     {'username':'oguerrero', 'password':'1234', 'nombre':'Oscar', 'apellido' : 'Guerrero', 'email' : 'oguerrerog@gmail.com', 'account_balance' : 0},
     {'username':'mjackson', 'password':'1234', 'nombre':'Michael', 'apellido' : 'Jackson', 'email' : 'jackson@gmail.com', 'account_balance' : 100000}
]

for datos in bdUsuarios: print(datos)

for clientes in bdUsuarios:
    print
    if clientes['username'] == "oguerrero":
        clientes['account_balance'] = "500"
print(bdUsuarios) 
transito = [{'username':'jimmy', 'password':'1234', 'nombre':'Michael', 'apellido' : 'Jackson', 'email' : 'jackson@gmail.com', 'account_balance' : 100000}]
bdUsuarios.append(transito)
print(bdUsuarios) 