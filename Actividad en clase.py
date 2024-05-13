import random
print("Semana 16 Ejercicio No 1")
A=[]
for i in range (10):
    r=random.randint(1,100)
    A.append(r)

promedio=0
for num in A:
    promedio+=num
promedio=promedio/len(A)
print(A)
print(len(A))
print("El promedio es:",promedio)

suma_par=0
suma_impar=0
for i in range(len(A)):
    if i%2==0:
        suma_par+=A[i]
    else:
        suma_impar+=A[i]
print("La suma par es: ",suma_par)
print("La suma impar es: ",suma_impar)

print("Semana 16: Ejercicio No. 2")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas"))
B=[]
for i in range(filas):
    temporal=[]
    for j in range(columnas):
        r=random.randint(0,1001)
        temporal.append(r)
    B.append(temporal)
print(B)
B[0][0]=500
print(B)

numeros_pares = 0
numeros_impares = 0
numero_mayor = B[0][0]
numero_menor = B[0][0]

for fila in B:
    for numero in fila:

        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
      
    if numero > numero_mayor:
        numero_mayor = numero

    if numero < numero_menor:
        numero_menor = numero
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
print("Número mayor:", numero_mayor)
print("Número menor:", numero_menor)