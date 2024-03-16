class Persona:
    
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo: "))
    
    def pagar_impuestos(self):
        self.imprimir_datos() 
        if self.sueldo > 3000:
            print("El empleado", self.nombre, "debe pagar impuestos.")
        else:
            print("El empleado", self.nombre, "no debe pagar impuestos.")

empleado = Empleado()
empleado.pagar_impuestos()
