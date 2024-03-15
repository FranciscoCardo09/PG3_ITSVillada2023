class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")

    def imprimir(self):
        print("Nombre:",self.nombre)


persona1=Persona()
persona1.imprimir()