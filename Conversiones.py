#Diego Rosales - 1206124
#Laboratorio Semana 9
metros = float(input("Ingrese la cantidad en metros: "))

millas = metros / 1609.34
kilometros = metros / 1000
pies = metros * 3.28
pulgadas = pies * 12

print("Resultado:")
print("Millas:", round(millas, 2))
print("Kilómetros:", round(kilometros, 2))
print("Pies:", round(pies, 2))
print("Pulgadas:", round(pulgadas, 2))