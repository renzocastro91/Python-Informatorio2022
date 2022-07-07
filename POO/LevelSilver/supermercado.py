"""
Supermercado
1er Requerimiento
Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre, precio, y si el mismo es parte del programa 
Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de 
un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:


precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9
El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos que comercializa y la suma total de los 
precios de los mismos.

2do Requerimiento
Suponga ahora que el descuento a aplicar en cada producto de primera necesidad puede ser distinto y se debe poder definir al momento de crear el mismo. 
Por ejemplo, el arroz puede ser un producto de primera necesidad con un descuento del 8%, mientras que leche podría ser otro producto de primera necesidad 
con un decuento del 11%. Esto es sólo un ejemplo. El descuento a aplicar en cada producto de primera necesidad debe ser configurable al momento de crearlo.
"""

# Clases\agentemaxo


class Super:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Supermercado {self.nombre} / Dirección: {self.direccion} / Teléfono: {self.telefono}"


class Producto:
    def __init__(self, codigo, nombre, precio, primera_necesidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.primera_necesidad = primera_necesidad
        self.precio_cuidado = False

    def __str__(self):
        if self.precio_cuidado == True:
            x = "Si"
        else:
            x = "No"
        if self.primera_necesidad == True:
            y = "Si"
        else:
            y = "No"
        return f"Codigo: {self.codigo} / Producto: {self.nombre} / Precio: {self.precio} / Precios Cuidados: {x} / Prod. Primera Necesidad: {y}"

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, nuevo):
        self.codigo = nuevo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevo):
        self.nombre = nuevo

    def getPrecio(self):
        return self.precio

    def setPrecio(self, nuevo):
        self.precio = nuevo

    def getPrimeraNecesidad(self):
        return self.primera_necesidad

    def setPrimeraNecesidad(self, nuevo):
        self.primera_necesidad = nuevo

    def getPrecioCuidado(self):
        return self.precio_cuidado

    def setPrecioCuidado(self, nuevo):
        self.precio_cuidado = nuevo

    def devolver_atributos(self):
        return [self.codigo, self.nombre, self.precio, self.primera_necesidad]


# Funciones
def obtener_txt_como_objetos(nombre_archivo):
    lista_articulos = []
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(",")
            cod = int(columnas[0])
            nom = columnas[1]
            pre = float(columnas[2])
            if columnas[3] == "1":
                prim = True
            else:
                prim = False
            objeto = Producto(cod, nom, pre, prim)
            lista_articulos.append(objeto)
        return lista_articulos


def cargar_lista_a_archivo(nombre_archivo, lista):
    with open(nombre_archivo, "w") as arch:
        for i in lista:
            x = i.devolver_atributos()
            booleano = x[3]
            if booleano:
                l = 1
            else:
                l = 0
            arch.write(f"{x[0]},{x[1]},{x[2]},{l}\n")
        arch.close()
        return arch


def buscarProd(lista, num):
    m = 0
    for i in lista:
        if i.getCodigo() == num:
            m = 1
            return i
    if m == 0:
        return 0


def registrar_compra(listaA, listaM):
    monto = 0
    while True:
        cod = int(input("Ingrese código de producto o 0 para finalzar el registro\t"))
        if cod != 0:
            x = buscarProd(listaA, cod)
            if x != 0:
                print("Producto Encontrado")
                print(x)
                c = input("Desea incluir al producto en precios cuidados? s o n\n\nIngrese:\t")
                if c.lower() == "s":
                    x.setPrecioCuidado(True)
                    monto = monto + x.getPrecio() * 0.9
                else:
                    monto = monto + x.getPrecio()
            else:
                print("Producto No encontrado")
        else:
            print("Fin del registro")
            print(f"Total a pagar: ${monto}")
            listaM.append(monto)
            break


def buscar_ultima_clave(lista):
    x = 0
    for i in lista:
        x = i.getCodigo()
    return x


def agregar_articulo(lista):
    cod = buscar_ultima_clave(lista) + 1
    nom = input("Ingrese Nombre Artículo:\t")
    pre = float(input("Ingrese precio:\t"))
    c = input("Es un producto de primera necesidad? s o n\n Ingrese:\t")
    if c.lower() == "s":
        pri = True
    else:
        pri = False
    objeto_nuevo = Producto(cod, nom, pre, pri)
    lista.append(objeto_nuevo)
    print("Artículo Agregado con éxito!")


def eliminar_articulo(lista):
    cod = int(input("Ingrese código de producto:\t"))
    x = buscarProd(lista, cod)
    if x != 0:
        lista.remove(x)
        print("Producto Eliminado!!")
    else:
        print("Producto No encontrado")


def modif_articulo(lista):
    cod = int(input("Ingrese código de producto:\t"))
    x = buscarProd(lista, cod)
    while True:
        if x != 0:
            op = input(
                "Que desea modificar? \n 1- Nombre del Producto \n 2- Precio \n 3- Es producto de primera necesidad \n 4- Pertenece a PC \n 5- Nada")
            if op == "1":
                nom = input("Ingrese nuevo nombre del artículo:\t")
                x.setNombre(nom)
                print("Producto Modificado")
            elif op == "2":
                pre = float(input("Ingrese nuevo precio:\t"))
                x.setPrecio(pre)
                print("Producto Modificado")
            elif op == "3":
                c = input("Es Producto de primera necesidad? s o n \n Ingreese:\t")
                if c.lower() == "s":
                    pri = True
                else:
                    pri = False
                x.setPrimeraNecesidad(pri)
                print("Producto Modificado")
            elif op == "4":
                c = input("El Producto pertenece a PC? s o n \n Ingreese:\t")
                if c.lower() == "s":
                    pc = True
                else:
                    pc = False
                x.setPrecioCuidado(pc)
                print("Producto Modificado")
            elif op == "5":
                print("Modificaciones terminadas")
                break


def estadistica(lista):
    cont_art = 0
    acu_mont = 0
    for i in lista:
        cont_art = cont_art + 1
        acu_mont = acu_mont + i.getPrecio()
    print(f"La cantidad de artículos que comercializa el Super es de : {cont_art}")
    print(f"El monto acumulado de todos los artículos que tenemos es de:  {acu_mont}")


def reindexar(lista):
    j = 1
    for i in lista:
        i.setCodigo(j)
        j += 1


# Programa
sup = Super("Don Atilo", "Av. 9 de Julio", 3652655565)
print("-------------------------------------------------------------")
print("Bienvenidos a mi programa!!")
print("-------------------------------------------------------------")
print(f"{sup}")
print("-------------------------------------------------------------")

lista_articulos = obtener_txt_como_objetos("lista_productos.txt")
monto_ingresado_dia = []

while True:
    op = input("Que desea hacer? \n 1- Registrar una compra \n 2- Buscar artículo \n 3- Agregar artículo \n 4- Eliminar Artículo \n 5- Modificar Artículo \n 6- Listar todos los productos \n 7- Salir \n\n Ingrese:\t")

    if op == "1":
        registrar_compra(lista_articulos, monto_ingresado_dia)
    elif op == "2":
        cod = int(input("Ingrese un código de producto:\t"))
        x = buscarProd(lista_articulos, cod)
        if x != 0:
            print("Producto Encontrado!!!")
            print(x)
        else:
            print("Producto Inexsistente")
    elif op == "3":
        agregar_articulo(lista_articulos)
    elif op == "4":
        eliminar_articulo(lista_articulos)
    elif op == "5":
        modif_articulo(lista_articulos)
    elif op == "6":
        for i in lista_articulos:
            print(i)
    elif op == "7":
        break
    print("-----------------------------------------------------------------------------------")
print("Gracias por utilizar el programa del Super!")
print("-----------------------------------------------------------------------------------")

estadistica(lista_articulos)
reindexar(lista_articulos)
cargar_lista_a_archivo("lista_productos.txt", lista_articulos)

print("-----------------------------------------------------------------------------------")
