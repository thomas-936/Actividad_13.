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

    def total_entregas(self, ):
        suma = 0
        for i in self.repartidores.values():
            suma += i.cantidad_paquetes
        return suma

    def promedio_entregas(self):
        total = self.total_entregas()
        cantididad = len(self.repartidores)
        promedio = total / cantididad
        if cantididad == 0:
            return  0
        return promedio


    def busqueda_secuecial(self, objetivo):
        lista = list(self.repartidores.values())
        for i in range(len(lista)):
            if lista[i].nombre == objetivo:
                return i
        return -1

    def buscar_repartidor(self):
        if not self.repartidores:
            print("No hay repartidores registrados")
            return
        nombre = input("Igrese el nombre del repartidor")
        busco = self.busqueda_secuecial(nombre)
        if busco != -1:
            print("El repartidor ha sido encontrado :) ")
            print(self.repartidores[nombre])
        else:
            print("El repartidor no ha sido encontrado")

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
            self.repartidores[codigo] = Repartidor(codigo, nombre, cantidad_paquetes, zona)

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista if x.cantidad_paquetes < pivote.cantidad_paquetes]
        iguales = [x for x in lista if x.cantidad_paquetes == pivote.cantidad_paquetes ]
        mayores = [x for x in  lista if x.cantidad_paquetes > pivote.cantidad_paquetes]
        return self.quick_sort(mayores) + iguales + self.quick_sort(menores)

    def menu(self):
        opcion = 0
        while opcion != 6:
            print("++MENU++")
            print("1. Agregar repartidor")
            print("2. Repartidores ordenados por número de entregas")
            print("3. Buscar repartidor por nombre")
            print("4. Mostrar Ranking de entregas")
            print("5. Estadisticas")
            print("6. Salir del programa")
            opcion = self.pedir_entero("Ingrese la opción que desee: ")
            match opcion:
                case 1:
                    self.agregar_repartidor()
                case 2:
                    lista_ordenada = self.quick_sort(list(self.repartidores.values()))
                    for repartidor in lista_ordenada:
                        print(repartidor)
                case 3:
                    self.buscar_repartidor()
                case 4:
                    print("El Ramking de entregas es: ")
                    lista_ranking = self.quick_sort(list(self.repartidores.values()))
                    for i in lista_ranking:
                        print(i)
                case 5:
                    print("Menu de estadisticas")
                    print("1. Total de paquestes entregados")
                    print("2. Promedio de entregas")
                    print("3. Repartidores con más entregas")
                    print("4. Repartidores con menos emtregas")
                    opcion_case5 = self.pedir_entero("Ingrese su opción: ")
                    match opcion_case5:
                        case 1:
                            self.total_entregas()
                        case 2:
                            self.promedio_entregas()

