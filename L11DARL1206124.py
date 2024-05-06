#Semana No. 11: Ejercicio 1
N=0
while N<=0:
    N=int(input("ingrese un número mayor a 0:"))
    if N<=0:
        print("El valor ingresado debe ser mayor a 0")
        print()
#El valor N ha sido leído
A=0
B=1
C=0
i=2
resultado=""
resultado=str(A)
if N>1:
    resultado+=(", "+str(B))
    while i<N:
        C=A+B
        resultado+=(", "+str(C))
        A=B
        B=C
        i=i+1
        print(resultado)
    else:
        print(resultado)

#Ejercicio 2
N=0
while n<=0:
    n=int(input("ingrese un número mayor a 0:"))
    if n<=0:
        print("El valor ingresado debe ser mayor a 0")
        print()
else:
    while i<n:
# Serie a:
        a=a + 1/i
        i=i+1
        print("Resultado de la serie a es:" , +a)
# Serie b
while i<n:
    b=b+ 1/2**i
    i=i+1
    print("Resultado de la serie b es:" , +b)

x=int(input("Ingrese un número"))
a1=int(input("Ingrese un número"))
n2=int(input("Ingrese un número"))
#Serie C
for i in range (0, n2 +1):
    c=c+(x**i)+a1**(n2-i)
    print("Resultado de la serie b es:" , +c)