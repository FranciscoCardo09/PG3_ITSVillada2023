class Operacion:

    def __init__(self):
        self.num1=int(input("Ingrese el valor del numero 1:"))
        self.num2=int(input("Ingrese el valor del numero 2:"))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.divicion()

    def suma(self):
        suma=self.num1+self.num2
        print("La suma es",suma)

    def resta(self):
        resta=self.num1-self.num2
        print("La rersta es",resta)

    def multiplicacion(self):
        multi=self.num1*self.num2
        print("El producto es",multi)

    def divicion(self):
        divi=self.num1/self.num2
        print("La division es",divi)

operacion1=Operacion()