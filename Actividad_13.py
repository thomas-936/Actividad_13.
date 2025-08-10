print("Actividad 13")


class Repartidor:
    def __init__(self,codigo, nombre, cantidad_paquetes, zona):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad_paquetes = cantidad_paquetes
        self.zona = zona

    def __str__(self):
        return (f"Nombre: {self.nombre}   "
                f"Paquetes: {self.cantidad_paquetes}   |"
                f"Zona: {self.zona}")

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = {}

    def pedir_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingrese un dato válido... :)")

    def agregar_repartidor(self):
        cantidad = self.pedir_entero("Ingrese la cantidad de repartidores que trabajaron hoy: ")
        for i in range(cantidad):
            print(f"----------------------")
            print(f"Repartidor {i+1}")
            while True:
                codigo = input("Ingrese el codigo del repartidor: ")
                if codigo in self.repartidores:
                    print("Este codigo ya ha sido resgistrado anteriormente....")
                else:
                    break
                nombre = input("Ingrese el nombre del rapartidor: ")
                cantidad_paquetes = self.pedir_entero("Ingrese la cantidad de paquetes entregados: ")
                zona = input("Ingrese la zona trabajada por el repartidor: ")
                self.repartidores[nombre]= Repartidor(codigo, nombre, cantidad_paquetes, zona)

    def quick_sort(self, lista):
        if len(lista) == 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista if x.cantidad_paquetes < pivote.catidad_paquetes]
        iguales = [x for x in lista if x.cantidad_paquetes == pivote.catidad_paquetes ]
        mayores = [x for x in  lista if x.cantidad_paquetes > pivote.catidad_paquetes]
        return self.quick_sort(mayores) + iguales + self.quick_sort(menores)

    def menu(self):
        opcion = 0
        while opcion != 6:
            print("++MENU++")
            print("1. Agregar repartidor")
            print("2. Ranking de entregas")
            print("3. Buscar repartidor por nombre")

