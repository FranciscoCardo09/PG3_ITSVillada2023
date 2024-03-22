def palindromo(palabra):
    palabra = palabra.lower()
    reversa_palabra = palabra[::-1]
    return reversa_palabra == palabra

palabra = input("Ingrese la palabra:")

print(palindromo(palabra))