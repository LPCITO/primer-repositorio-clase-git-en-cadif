print("ingrese su edad")
edad=int(input())
print("eres estudiante s/n")
estudiante=input().upper()
precio=1000
porc=0
if edad>0:
    if edad<3:
        porc=1 
    elif edad<5:
        porc=0.5   
    elif edad<10:
        porc=0.2    
    elif edad<54:
        porc=0.3
    else:
        porc=0

    if estudiante=="s":
        if porc<0.25:
            porc=0.25

    metodo=precio*porc
    total=precio-metodo
    print(f"precio de entrada sin descuento{precio}")
    if porc>0:
        print(f"el porcentaje de descuento {porc}")
        print(f"monto descuento{metodo}")
       
    print(f"el porcent5aje de descuento  el total a pagar por la entrada {total} ")
else:
    print("la edad debe ser positiva")