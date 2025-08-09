print("Actividad 13")


class Repartidor:
    def __init__(self, nombre, cantidad_paquetes, zona):
        self.nombre = nombre
        self.cantidad_paquetes = cantidad_paquetes
        self.zona = zona

    def __str__(self):
        return (f"Nombre: {self.nombre} |"
                f"Paquetes: {self.cantidad_paquetes}|"
                f"Zona: {self.zona}")

class EmpresaMensajeria:
    def __init__(self):
        self.repartidores = {}

    def agregar_repartidor(self):
        cantidad = int(input("Ingrse la cantidada de repartodores que "))
        for i in range(cantidad):
            print(f"----------------------")
            print(f"Repartidor {i+1}")
            while True:
                nombre = input("Ingrse el nombre del rapartidor: ")
                if nombre in self.repartidores:
                    print("Este repartidor ya ha sido registrado")
                else:
                    break

                cantidad_paquetes = int(input("Ingrse la cantidad de paquetes: "))
                zona = input("Ingrese la zona trbajada por el repartidor: ")
                self.repartidores[nombre]= Repartidor(nombre, cantidad_paquetes, zona)

