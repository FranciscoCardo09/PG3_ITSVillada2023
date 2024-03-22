def orden(lista_numeros):
    n = len(lista_numeros)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista_numeros[j] < lista_numeros[j + 1]:
                lista_numeros[j], lista_numeros[j + 1] = lista_numeros[j + 1], lista_numeros[j]
    return lista_numeros

lista_numeros = [7, 18, 2, 4, 5]

lista_ordenada = orden(lista_numeros)

print("Lista Original:", lista_numeros)
print("Lista Ordenada de Mayor a Menor:", lista_ordenada)
