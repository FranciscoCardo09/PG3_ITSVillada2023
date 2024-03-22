class Familia:
    def __init__(self, nombre_pa, nombre_ma, hijos=[]):
        self.nombre_pa = nombre_pa
        self.nombre_ma = nombre_ma
        self.hijos = hijos
    
    def __str__(self):
        hijos_str = ', '.join(self.hijos)
        return f"Papá: {self.nombre_pa}, Mamá: {self.nombre_ma}, Hijos: {hijos_str}"

familia = Familia("Messi", "Antonela", ["Mateo", "Ciro", "Thiago"])
print(familia)