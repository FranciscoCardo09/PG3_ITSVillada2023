def vocales(frase):
    contador = 0
    for caracter in frase:
        if caracter.lower() in "aeiou" :
            contador += 1
    return contador

frase = input("Ingrese la frase: ")

cantidad_de_vocales = vocales(frase)
print(f"La frase tiene {cantidad_de_vocales} vocales")