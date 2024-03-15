class Triangulo:

    def inicializar(self,lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", mayor)

    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")

triangulo1=Triangulo()
triangulo1.inicializar(4, 4, 4)
triangulo1.imprimir_lado_mayor()
triangulo1.equilatero()

triangulo2=Triangulo()
triangulo2.inicializar(5, 9, 1)
triangulo2.imprimir_lado_mayor()
triangulo2.equilatero()