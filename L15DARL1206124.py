import math
#Definición de funciones
def menu ():
    print("Elija una opción: ")
    print("a. Area del triangulo")
    print("b. Area del cuadrado")
    print("c. Area del rectangulo")
    print("d. Area del circulo")
    print("e. Salir")
    opcion=input()
    return opcion

def ObtenerAreaTriangulo(base, altura):
    area=(base*altura)/2
    return (base*altura)/2
def ObtenerAreaCuadrado(lado):
    return lado**2
def ObtenerAreaRectangulo(base,altura):
    return base*altura
def ObtenerAreaCirculo(radio):
    return math.pi*radio**2
#Interacción con usuario
print("Semana No. 15: Ejercicio 1")
match(menu()):
    case "a":
        print("El area del triangulo es: ",ObtenerAreaTriangulo(float(input("Ingrese la base")),float(input("Ingrese la altura"))))
    case "b":
        print("El area del cuadrado es: ",ObtenerAreaCuadrado(float(input("Ingrese el lado del cuarado: "))))
    case "c":
        print("El area del rectangulo es: ",ObtenerAreaRectangulo(float(input("Ingrese la base")),float(input("Ingrese la altura"))))
    case "d":
        print("El area del circulo es: ",round(ObtenerAreaCirculo(float(input("Ingrese el radio del circulo: "))),3))


X = 0
Y = 0


def MoverHaciaArriba():
    global Y
    Y += 1


def MoverHaciaAbajo():
    global Y
    Y -= 1


def MoverHaciaLaDerecha():
    global X
    X += 1

def MoverHaciaLaIzquierda():
    global X
    X -= 1

def ManejarEntrada(opcion):
    match opcion:
        case "a":
            MoverHaciaArriba()
        case "b":
            MoverHaciaAbajo()
        case "c":
            MoverHaciaLaIzquierda()
        case "d":
            MoverHaciaLaDerecha()
        case "e":
            print("Coordenadas finales del personaje:", X, ",", Y)
            return True
        case _:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    return False

def main():
    print("Semana No. 12: Ejercicio 2")

    while True:
        print("\nMenú:")
        print("a. Sube")
        print("b. Baja")
        print("c. Izquierda")
        print("d. Derecha")
        print("e. Salir")

        opcion = input("Selecciona una opción: ")

        if ManejarEntrada(opcion):
            break

if __name__ == "__main__":
    main()