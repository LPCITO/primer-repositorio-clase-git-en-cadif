print("ingresa tus notas")
n1=float(input("nota primer lapso    "))
n2=float(input("nota segundo lapso   "))
n3=float(input("nota tercer lapso    "))
promedio=(n1+n2+n3)/3
print(f"tu promedio es   {round  (promedio)}")
if promedio>17:
    print("decente")
else:
    print("reprobado")