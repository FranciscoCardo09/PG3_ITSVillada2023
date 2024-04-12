def mostrar_nombre_mes():
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    while True:
        try:
            numero_mes = int(input("Ingrese el número de mes (1-12): "))
            nombre_mes = meses[numero_mes - 1]

            print("El mes es:", nombre_mes)

            break 

        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            
        except IndexError:
            print("Error: El número de mes debe estar entre 1 y 12.")

mostrar_nombre_mes()
