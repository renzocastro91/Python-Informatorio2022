#Clases

class Mate:
    def __init__(self,cant_cebadas):
        self.cant_cebadas = cant_cebadas
        self.estado = "Vacio"

    def __str__(self):
        print("-------------------------------------------------------------------------")
        return f"Cantidad de Cebadas: {self.cant_cebadas} / Estado: {self.estado}"

    def getCant_cebadas(self):
        return self.cant_cebadas
    
    def cebar(self):
        print("-------------------------------------------------------------------------")
        if self.cant_cebadas != 0:
            if self.estado == "Lleno":
                print("Cuidado!! Te quemaste!")
            else:
                self.estado = "Lleno"
                print("Cebaste el mate")
        else:
            if self.estado == "Lleno":
                print("Cuidado!! Te quemaste!")
            else:
                self.estado = "Lleno"
                print("Cebaste el mate, pero está lavado")

    def beber(self):
        print("-------------------------------------------------------------------------")
        if self.cant_cebadas != 0:    
            if self.estado == "Vacio":
                print("El mate está vacío, no puedes tomar")
            else:
                self.estado = "Vacio"
                self.cant_cebadas = self.cant_cebadas - 1
                print("Tomaste el mate")
        else:
            if self.estado == "Vacio":
                print("El mate está vacío, no puedes tomar")
            else:
                print("El mate está lavado")
                self.estado = "Vacio"
                print("Tomaste el mate")
