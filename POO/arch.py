class Nota:
    def __init__(self):
        self.nota = []

    def cargar_nota(self,nuevo):
        self.nota.append(nuevo)

    def promedio(self):
        if self.nota == []:
            return "No hay notas para hacer promedio"
        else:
            return sum(self.nota) / len(self.nota)

n1 = Nota()
print(n1.nota)
print(f"Promedio --> {n1.promedio()}")
n1.cargar_nota(8)
n1.cargar_nota(9)
n1.cargar_nota(10)
print(n1.nota)
print(f"Promedio --> {n1.promedio()}")