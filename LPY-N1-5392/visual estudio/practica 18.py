print("bienvenido a la tienda junmp-adidas")
print("como te llamas")
nombre=input()
modelo=input("cual modelo deseas")
talla=int (input("que talla eres"))
precio=100
descuento=precio*0.25
total=precio-descuento
print(f"""
cliente: {nombre}
modelo: {modelo}
talla:{talla}
precio:{precio}
descuemto: {descuento}
total: {total}
""")