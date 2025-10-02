print("cuantio vendiste")
monto=float(input())
print("que edad tienes")
edad=int(print())
print("ingrese su genero f/m")
genero=input()
salario=5000
if monto>0 and monto>75000:
    porc=0.05
elif monto>9000 and monto<200000:
    porc=0.07
elif monto>300000 and monto<1000000:
    porc=0.08
elif monto>1500000:
    porc=0.01
else:
    porc=0.06

if (edad>=55 and genero=="f")or (edad>=60 and genero=="m"):
    bono=40000
else:
    bono=0

comision=monto*porc
salariof=salario+comision+bono
print(f"""
salario: {salario}
vendio: {monto}
% comision: {porc}
comision: {comision}
bono: {bono}
salario total: {salariof}
""")