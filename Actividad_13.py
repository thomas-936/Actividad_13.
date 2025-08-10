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

    def mas_entregas(self):
        if not self.repartidores:
            print("No hay repartidores registrados")
            return []
        max = -1
        for j in self.repartidores.values():
            if j.cantidad_paquetes > max:
                max = j.cantidad_paquetes

        repartidores_max = []
        for i in self.repartidores.values():
            if i.cantidad_paquetes == max:
                repartidores_max.append(i)
        return repartidores_max

    def menos_entregas(self):
        if not self.repartidores.values():
            print("No hay repartidores registrados")
            return []
        min = 15
        for i in self.repartidores.values():
            if i.cantidad_paquetes < min:
                min = i.cantidad_paquetes

        repartidores_min = []
        for j in self.repartidores.values():
            if j.cantidad_paquetes == min:
                repartidores_min.append(j)
        return repartidores_min

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
        nombre = input("Ingrese el nombre del repartidor: ")
        encontrado = None
        for repartidor in self.repartidores.values():
            if repartidor.nombre == nombre:
                encontrado = repartidor
                break
        if encontrado:
            print("El repartidor ha sido encontrado :) ")
            print(encontrado)
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
                    print("5. Volver al menú principal")
                    opcion_case5 = self.pedir_entero("Ingrese su opción: ")
                    match opcion_case5:
                        case 1:
                            total = self.total_entregas()
                            print(f"El total de entregas es: {total}")
                        case 2:
                            promedio = self.promedio_entregas()
                            print(f"El promedio de entregas es: {promedio}")
                        case 3:
                            mas_entregas = self.mas_entregas()
                            print("Los repartidores con más entregas son:")
                            for i in mas_entregas:
                                print(i)
                        case 4:
                            menos_entregas = self.menos_entregas()
                            print("Los repartidores con menos de 15 entregas son: ")
                            for j in menos_entregas:
                                print(j)
                        case 5:
                            pass
                        case _:
                            print("Ingrese un opción válida")
                case 6:
                    print("Saliendo del programa... ")
                case _:
                    print("Ingrese una opción válida")