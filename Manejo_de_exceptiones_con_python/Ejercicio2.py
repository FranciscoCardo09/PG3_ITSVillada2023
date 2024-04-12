def division():
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            resultado = num1 / num2

            print("El resultado de dividir", num1, "y", num2, "es:", resultado)

            continuar = input("¿Quiere seguir sumando valores? (s/n): ")

            if continuar.lower() != 's':
                break

        except ValueError:
            print("Error: Por favor, ingrese solo números.")
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")

division()
