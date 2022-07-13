"""
Una pizzería de la ciudad ofrece a sus clientes una amplia variedad de pizzas de fabricación propia, de varios tamaños (8, 10 y 12 porciones). 

Los clientes tienen a disposición un menú que describe para cada una de las variedades, el nombre, los ingredientes y el precio según el tamaño y 
el tipo (a la piedra, a la parrilla, de molde) de la pizza. Los clientes realizan sus pedidos en el mostrador. El pedido debe contener el nombre del Cliente, 
para llamarlo cuando su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, la fecha del pedido, la hora en la que el pedido debe entregarse y 
la demora estimada informada al cliente. El pedido va a la cocina y cuando está preparado se informa al que lo tomó para que se genere la factura correspondiente 
y se le entregue el pedido al cliente. 

El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la siguiente información: 

Variedades y tipos de pizzas más pedidas por los clientes. 

Ingresos (recaudaciones) por períodos de tiempo. 

Pedidos (cantidad y monto) por períodos de tiempo. 

Implementar un programa en Python que resuelva este caso de estudio a través de clases y métodos.

Edit Renzo Castro: Agrego una condición, el precio de la pizza va a ser el base siempre y cuando la cantidad de ingredientes no supere los 3, si supera los 3 se añade un aumento de
25 pesos por ingrediente extra.
El tiempo de entrega será: hasta 2 pizzas 1 hora, y por cantidad superior a eso, se agrega 20 min por pizza

"""
# Clases
from datetime import datetime


class Pizza:
    def __init__(self, nombre, ingredientes, tipo):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = 0
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getIngredientes(self):
        return self.ingredientes

    def setIngredientes(self, nuevo):
        self.ingredientes = nuevo

    def getPrecio(self):
        return self.precio

    def setPrecio(self, nuevo):
        self.precio = nuevo

    def getTipo(self):
        return self.tipo

    def setTipo(self, nuevo):
        self.tipo = nuevo

    def __str__(self):
        return f"Nombre: {self.nombre} / Ingredientes: {self.ingredientes} / Tipo: {self.tipo}"


class Pizza_8_Porciones(Pizza):
    def __init__(self, nombre, ingredientes, tipo):
        super().__init__(nombre, ingredientes, tipo)
        self.precio = 125

    def __str__(self):
        return super().__str__() + f" / Tamaño: 8 Porciones / Precio: ${self.precio}"


class Pizza_10_Porciones(Pizza):
    def __init__(self, nombre, ingredientes, tipo):
        super().__init__(nombre, ingredientes, tipo)
        self.precio = 200

    def __str__(self):
        return super().__str__() + f" / Tamaño: 10 Porciones / Precio: ${self.precio}"


class Pizza_12_Porciones(Pizza):
    def __init__(self, nombre, ingredientes, tipo):
        super().__init__(nombre, ingredientes, tipo)
        self.precio = 275

    def __str__(self):
        return super().__str__() + f" / Tamaño: 12 Porciones / Precio: ${self.precio}"


class Pedido:
    def __init__(self, nombre, telefono, cantidad, monto, tamanio, fecha, hora, hora2, tiempo_demora, pizza, cerrada=False):
        self.nombre_cli = nombre
        self.telefono = telefono
        self.pizza = pizza
        self.cantidad_pizza = cantidad
        self.monto_tot = monto
        self.tamanio = tamanio
        self.fecha_pedido = fecha
        self.hora_pedido = hora
        self.hora_entrega = hora2
        self.demora = tiempo_demora
        self.cerrada = cerrada

    def __str__(self):
        return f"Pedido: --> Nombre Cliente: {self.nombre_cli} \n Telefono: {self.telefono} \n Pizza: {self.pizza} \n Cantidad Pizzas: {self.cantidad_pizza} \n Tamaño: {self.tamanio} \n Fecha Pedido: {self.fecha_pedido} \n Hora Pedido: {self.hora_pedido} \n Hora Entrega: {self.hora_entrega} \n Demora: {self.demora} hs"

    def setCerrada(self):
        self.cerrada = True

# Funciones


def menu_cocina(lista_pedidos, lista_monto):
    print("--------------------------------------------")
    print("Sistema de la Cocina")
    print("--------------------------------------------")
    print("Ha llegado un nuevo pedido!!!!")
    print(lista_pedidos[-1])
    while True:
        print("Desea cerrar el pedido? s o n")
        op = input("Ingrese:\t")
        if op.lower() == "s":
            lista_pedidos[-1].setCerrada()
            break
    print("Pedido Cerrado!!!! Envío del Pedido en curso!")


def menu_cliente(lista_p, lista_pedidos, lista_monto):
    print("--------------------------------------------------------------")
    print("Bienvenidos al Menú del Cliente")
    print("--------------------------------------------------------------")
    nom_cli = input("Ingrese su nombre\t")
    tel = int(input("Ingrese su Teléfono\t"))

    op = input("Seleccione el tipo de Pizza que desea ordenar: \n 1- Margarita \n 2- Pepperoni \n 3- Cuatro Estaciones \n 4- Con Champiniones \n 5- Hawaiana \n 6- Marinara \n 7- Napolitana \n 8- Neoyorquina \n 9- Fugazzeta \n 10- Cuatro Quesos \n Ingrese:\t")

    if op == "1":
        nombre = "Margarita"
        ingredientes = ["Albahaca", "Mozzarella", "Tomate"]
    elif op == "2":
        nombre = "Pepperoni"
        ingredientes = ["Pepperoni", "Salame",
                        "Tomate", "Mozzarella", "Albahaca"]
    elif op == "3":
        nombre = "Cuatro Estaciones"
        ingredientes = ["Alcauciles", "Jamón", "Aceitunas",
                        "Champiniones", "Mozzarella", "Tomate"]
    elif op == "4":
        nombre = "Con Champiniones"
        ingredientes = ["Champiniones", "Queso", "Tomate", "Portobello"]
    elif op == "5":
        nombre = "Hawaiana"
        ingredientes = ["Ananá", "Mozzarella", "Tomate", "Jamón"]
    elif op == "6":
        nombre = "Marinara"
        ingredientes = ["Tomates", "Ajo", "Cebollas",
                        "Hierbas aromáticas", "Orégano", "Aceite de Olivda"]
    elif op == "7":
        nombre = "Napolitana"
        ingredientes = ["Tomate", "Mozzarella", "Anchoas",
                        "Alcaparras", "Ajo", "Aceite de Oliva"]
    elif op == "8":
        nombre = "Neoyorquina"
        ingredientes = ["Tomate", "Queso", "Verduras Varias", "Carne", "Jamón"]
    elif op == "9":
        nombre = "Fugazzeta"
        ingredientes = ["Queso", "Cebolla", "Aceitunas"]
    elif op == "10":
        nombre = "Cuatro Quesos"
        ingredientes = ["Mozzarella", "Gorgonzala",
                        "Parmesano", "Fontina", "Tomate"]

    op = input(
        "Ingrese el tipo: \n 1- A la piedra \n 2- A la parrilla \n 3- De molde \n Ingrese:\t")

    if op == "1":
        tipo = "A la piedra"
    elif op == "2":
        tipo = "A la parrilla"
    elif op == "3":
        tipo = "De molde"

    tam = input(
        "Ingrese el tamaño de la pizza: \n 1- 8 Porciones \n 2- 10 Porciones \n 3- 12 Porciones \n Ingrese:\t")

    if tam == "1":
        tamanio = "8 Porciones"
        precio_extra = 0
        if len(ingredientes) > 3:
            x = len(ingredientes) - 3
            precio_extra = x * 25
        pizza = Pizza_8_Porciones(nombre, ingredientes, tipo)
        precio = pizza.getPrecio()
        pizza.setPrecio(precio + precio_extra)
    elif tam == "2":
        tamanio = "10 Porciones"
        precio_extra = 0
        if len(ingredientes) > 3:
            x = len(ingredientes) - 3
            precio_extra = x * 25
        pizza = Pizza_10_Porciones(nombre, ingredientes, tipo)
        precio = pizza.getPrecio()
        pizza.setPrecio(precio + precio_extra)
    elif tam == "3":
        tamanio = "12 Porciones"
        precio_extra = 0
        if len(ingredientes) > 3:
            x = len(ingredientes) - 3
            precio_extra = x * 25
        pizza = Pizza_10_Porciones(nombre, ingredientes, tipo)
        precio = pizza.getPrecio()
        pizza.setPrecio(precio + precio_extra)

    lista_p.append(pizza)

    cant = int(input("Cuántas pizzas desea pedir?\t"))
    hora_entrega = 60
    if cant > 2:
        x = cant - 2
        v = x * 20
        hora_entrega = hora_entrega + v

    monto_tot = pizza.getPrecio() * cant

    lista_monto.append(monto_tot)

    fecha_pedido = datetime.today().strftime('%Y-%m-%d')

    hora = datetime.now()

    hora_pedido = hora.time()

    demora = 30

    pedido = Pedido(nom_cli, tel, cant, monto_tot, tamanio,
                    fecha_pedido, hora_pedido, hora_entrega, demora, pizza)

    lista_pedidos.append(pedido)

    print("Muchas gracias por utilizar la APP de Pizzería Don Carlos")

    menu_cocina(lista_pedidos, lista_monto)


def buscar_pizzas_variedades_mas_pedidas(lista):
    print("Variedad Mas vendida del día")
    x = []
    y = []
    for i in lista:
        x.append(i.getNombre())
        y.append(i.getTipo())
    print(max(set(x), key=x.count))
    print("Tipo de Pizza mas vendidas del día")
    print(max(set(y), key=x.count))


def recaudacion_del_dia(lista):
    print("Recaudación del día")
    print(f"${sum(lista)}")


def cant_pedidos_monto(lista1, lista2):
    print(f"Cantidad de Pedidos del día --> {len(lista2)}")
    recaudacion_del_dia(lista1)


# Programa
print("Bienvenidos a la APP de Pizzería Don Carlos!!!")

lista_monto = []
lista_pedido = []
lista_pizza = []

while True:
    op = input("Que desea hacer? \n 1- Realizar pedido \n 2- Salir \n Ingrese:\t")
    if op == "1":
        menu_cliente(lista_pizza, lista_pedido, lista_monto)
    elif op == "2":
        break
    print("-----------------------------------------------------------")
# Variedades y tipos de pizzas más pedidas por los clientes.
buscar_pizzas_variedades_mas_pedidas(lista_pizza)


# Ingresos (recaudaciones) por períodos de tiempo.
recaudacion_del_dia(lista_monto)


# Pedidos (cantidad y monto) por períodos de tiempo.
cant_pedidos_monto(lista_monto, lista_pedido)
