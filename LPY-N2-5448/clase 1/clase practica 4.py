for i in range(1,5):
    print("tipo de precio")
    print("a -> 80")
    print("b -> 105")
    print("c -> 250")
    print("cual deseas llevar")
    tipo=input().upper()
    print("cuantos deseas llevar")
    cant=int(input())
    if tipo=="a":
        precio= 80
    elif tipo=="b":
        precio= 105
    elif tipo=="c":
        precio= 250
    else:
        precio=0
    total=precio*cant
    if cant>0:
        if precio>0:
            print(f"tipo de pantalon: {tipo}")
            print(f"precio: {precio}")
            print(f"total: {total}")
        else:("tipo de pantalon invalido")
    else:
        print("la cantidad debe ser positiva")