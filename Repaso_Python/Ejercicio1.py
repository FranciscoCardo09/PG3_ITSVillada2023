def busqueda(lista_numeros, busqueda):
    for i in range(len(lista_numeros)):
        if busqueda == lista_numeros[i]:
            return i
    return None

lista_numeros = [ 7, 18, 2, 4, 5]

numero = int(input("Ingrese el número que desea buscar: "))

resultado = busqueda(lista_numeros, numero)

if resultado != None:
    print(f"El elemento {numero} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {numero} no está en la lista.")
