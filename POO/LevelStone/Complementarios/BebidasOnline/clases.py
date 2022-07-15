#Clases
class Bebida:
    def __init__(self,identificador, litros, marca,precio):
        self.id = identificador
        self.litros = litros
        self.marca = marca
        self.precio = precio
    
    def __str__(self):
        return f"Id: {self.id} / Cant. Litros: {self.litros} / Marca: {self.marca} / Precio: ${self.precio}"

    def getId(self):
        return self.id
    
    def setId(self,nuevo):
        self.id = nuevo

    def getLitros(self):
        return self.litros
    
    def setLitros(self,nuevo):
        self.litros = nuevo
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self,nuevo):
        self.marca = nuevo
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,nuevo):
        self.precio = nuevo
    
class AguaMineral(Bebida):
    def __init__(self, identificador, litros, marca, precio, origen):
        super().__init__(identificador, litros, marca, precio)
        self.origen = origen
    
    def __str__(self):
        return super().__str__() + f" / Origen: {self.origen}"

    def getOrigen(self):
        return self.origen

    def setOrigen(self,nuevo):
        self.origen = nuevo

    
class Gaseosa(Bebida):
    def __init__(self, identificador, litros, marca, precio, porazucar):
        super().__init__(identificador, litros, marca, precio)
        self.porazucar = porazucar
        self.promo = False

    def __str__(self):
        if self.promo:
            x = "Si"
        else:
            x = "No"
        return super().__str__() + f" / Porcentaje Azucar: {self.porazucar} / Promoción: {x}"

    def getPorazucar(self):
        return self.porazucar

    def setPorazucar(self,nuevo):
        self.porazucar = nuevo

    def getPromo(self):
        return self.promo
    
    def setPromo(self):
        self.promo = True
    
class Almacen:
    def __init__(self,listabebidas=[]):
        self.listabebidas = listabebidas

    def mostrarBebidas(self):
        print("---------------------------------------------")
        print("Lista de Bebidas")
        for i in self.listabebidas:
            print(i)


    def calcularPrecioTotal(self):
        monto_tot = 0
        for i in self.listabebidas:
            monto_tot = monto_tot + i.getPrecio()
        return monto_tot
    
    def calcularPrecioMarca(self,marca):
        monto_tot = 0
        for i in self.listabebidas:
            if i.getMarca() == marca:
                monto_tot = monto_tot + i.getPrecio()
        return monto_tot
    
    def agregarBebida(self,objeto):
        self.listabebidas.append(objeto)

    def buscarProducto(self,lista,iden):
        marca = 0
        for i in lista:
            if i.getId() == iden:
                return i 
        if marca == 0:
            return 0

    def eliminarBebida(self,identificador):
        x = self.buscarProducto(self.listabebidas,identificador)
        if x != 0:
            print("---------------------------------------------")
            self.listabebidas.remove(x)
            print("Bebida Eliminada de la lista")
        else:
            print("---------------------------------------------")
            print("Bebida No encontrada")

    def mostrarInfoBebida(self,iden):
        x = self.buscarProducto(self.listabebidas,iden)
        if x != 0:
            print("---------------------------------------------")
            print("Producto Encontrado!")
            print(x)
        else:
            print("---------------------------------------------")
            print("Bebida No Encontrada")

    def devolverultimoid(self):
        c = 0
        for i in self.listabebidas:
            c = i.getId()
        return c            