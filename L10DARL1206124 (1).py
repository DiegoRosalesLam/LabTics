
print("Semana No. 10: Ejercicio 1")

numero_mes = int(input("Ingrese el número de mes (1-12): "))

if numero_mes < 1 or numero_mes > 12:
    print("Error: El número a ingresar debe estar entre 1 y 12")
else:
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    
    
    print("Mes:", meses[numero_mes])

print("Semana No. 10: Ejercicio 2")
a= int(input("Ingrese un primer numero mayor a 0\n"))
b= int(input("Ingrese un segundo numero mayor a 0\n"))
c= int(input("Ingrese un tercer numero mayor a 0\n"))

if(a<=0 or b<=0 or c<=0):
    print("Error ingrese numeros mayores a 0")
if (a>b):
    if(a>c):
        print("A es el mayor")
    else: 
        if(a == c):
            print("A es mayor a B, A es igual a C")
        else:
            print("A es mayor a B y menor que C")
elif (a == b):
    if(a > c):
        print("A es igual a B y A es mayor que C")
    else :
        if(a==c):
            print("Todos son iguales")
        else:
            print("A es igual a B y es menor que c")
elif (b>c):
    print("B es mayor a A y mayor a C")
else: 
    if(b==c):
        print("B es igual a C y B igual C mayor que A")
    else:
        print("B mayor que A y A igual C ")
        
print("Semana No. 10: Ejercicio 3")
def calcular_signo_zodiacal(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    else:
        return "Capricornio"

dia = int(input("Ingrese el día de su fecha de nacimiento: "))
mes = int(input("Ingrese el mes de su fecha de nacimiento (en números): "))
anio = int(input("Ingrese el año de su fecha de nacimiento: "))

signo_zodiacal = calcular_signo_zodiacal(dia, mes)

print("Su signo zodiacal es:", signo_zodiacal)