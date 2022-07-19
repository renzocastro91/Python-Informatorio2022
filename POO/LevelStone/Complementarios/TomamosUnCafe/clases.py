#Clases

class Cafetera:
    def __init__(self):
        self.__capacidad_max = 200
        self.__cantidad_actual = 0

    def __str__(self):
        print("-----------------------------------------------------------------------------------------")
        print("Estado de la Cafetera")
        return f"Capacidad Máxima: {self.__capacidad_max} / Cantidad Actual: {self.__cantidad_actual}"
    
    def llenarCafetera(self):
        print("-----------------------------------------------------------------------------------------")
        if self.__cantidad_actual == self.__capacidad_max:
            print("La cafetera no se puede llenar, porque ya está llena")
        else:
            self.__cantidad_actual = self.__capacidad_max
            print("Cafetera LLena!!!")
    
    def servirTaza(self,num):
        print("-----------------------------------------------------------------------------------------")
        if self.__cantidad_actual > 0:    
            if num > self.__cantidad_actual:
                print(f"Se sirvió la taza con capacidad: {self.__cantidad_actual}")
                self.__cantidad_actual = 0
            else:
                print(f"Se sirvió la taza con capacidad: {num}")
                self.__cantidad_actual = self.__cantidad_actual - num
        else:
            print("La cafetera está vacía, no puedo servir mas")

    def vaciarCafetera(self):
        print("-----------------------------------------------------------------------------------------")
        self.__cantidad_actual = 0
        print("La cafetera se vació")
    
    def agregarCafe(self,num):
        print("-----------------------------------------------------------------------------------------")
        if num + self.__cantidad_actual > self.__capacidad_max:
            resto = num
            for i in range(num):
                if self.__cantidad_actual < self.__capacidad_max:    
                    self.__cantidad_actual = self.__cantidad_actual + 1
                    resto = resto - 1
                else:
                    break
            print(f"Se llenó la cafetera, y sobró una cantidad de café igual a: {resto}")
        else:
            self.__cantidad_actual = self.__cantidad_actual + num
            print(f"Se agregó la cantidad de café igual a: {num}")
        