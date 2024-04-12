def escribir_string_en_archivo(string, nombre_archivo):
    try:
        with open(nombre_archivo, "a") as archivo:  # Abrir en modo de agregado
            archivo.write(string + "\n")

    except TypeError as e:
        print("Error:", e)
        print("No se puede escribir un entero en el archivo de texto.")

    except Exception as e:
        print("Error:", e)
        print("Ha ocurrido un error al escribir en el archivo.")

while True:
    string = input("Ingrese el string que desea almacenar en el archivo (o 'fin' para terminar): ")
    if string.lower() == 'fin':
        break
    nombre_archivo = "archivo.txt"
    escribir_string_en_archivo(string, nombre_archivo)
