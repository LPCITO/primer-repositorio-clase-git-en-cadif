print("calculo del salario")
print("como te llamas")
nombre=input()
print("cuanto vendiste este mes?")
monto=int(input())
print("horas trabajasa")
salariobase=100
comision=monto*0.3
montohoras=horas*5
deducciones=salariobase*0.5
salario=salariobase+comision+montohoras-deducciones
#salidas
print("""
empleado :{nombre}
""")