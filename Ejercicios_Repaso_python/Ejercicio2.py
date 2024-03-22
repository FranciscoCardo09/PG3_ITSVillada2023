def añobisiesto(año):
    if año%100 != 0:
        if año%4 == 0:
            return print("bisiesto")
        else:
            return print("No es bisiesto")
    elif año%400 == 0:
        return print("bisiesto")
    else:
        return print("No es bisiesto")

año_ingresado = int(input("Ingrese el año que desea saber: "))

añobisiesto(año_ingresado)
