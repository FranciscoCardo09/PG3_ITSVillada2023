def dibujar(ancho, alto, caracter, forma):
    
    if forma == "rectangulo":
        for i in range(alto):
            fila = caracter * ancho
            print(fila)
            
    elif forma == "triangulo":
        for i in range(1, alto + 1):
            fila = caracter * i
            print(fila)

ancho = int(input("Ingrese el ancho: "))
alto = int(input("Ingrese el alto: "))
caracter = input("Ingrese el caracter: ")
forma = input("Ingrese la forma (rectangulo o triangulo): ")

dibujar(ancho, alto, caracter, forma)