# Definimos la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, costo_por_dia):
        # Atributos básicos de un vehículo
        self.marca = marca
        self.modelo = modelo
        self.costo_por_dia = costo_por_dia
        self.disponible = True  # Todos los vehículos están disponibles al inicio

    def mostrar_info(self):
        # Muestra la información básica del vehículo
        return f"{self.marca} {self.modelo} - Costo por día: ${self.costo_por_dia}"

    def rentar(self):
        # Marca el vehículo como no disponible si está disponible
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        # Marca el vehículo como disponible nuevamente
        self.disponible = True

# Definimos la clase Cliente
class Cliente:
    def __init__(self, nombre):
        # Atributos básicos de un cliente
        self.nombre = nombre
        self.vehiculo_rentado = None

    def rentar_vehiculo(self, vehiculo):
        # Permite al cliente rentar un vehículo si está disponible
        if vehiculo.rentar():
            self.vehiculo_rentado = vehiculo
            print(f"{self.nombre} ha rentado el {vehiculo.marca} {vehiculo.modelo}.")
        else:
            print("Lo siento, el vehículo no está disponible.")

    def devolver_vehiculo(self):
        # Permite al cliente devolver el vehículo rentado
        if self.vehiculo_rentado:
            self.vehiculo_rentado.devolver()
            print(f"{self.nombre} ha devuelto el {self.vehiculo_rentado.marca} {self.vehiculo_rentado.modelo}.")
            self.vehiculo_rentado = None
        else:
            print("No hay vehículo para devolver.")

# Lista para almacenar los vehículos disponibles
vehiculos_disponibles = []

def agregar_vehiculo(vehiculo):
    # Agrega un vehículo a la lista de vehículos disponibles
    vehiculos_disponibles.append(vehiculo)
    print(f"{vehiculo.marca} {vehiculo.modelo} ha sido agregado al lote.")

def mostrar_vehiculos_disponibles():
    # Muestra todos los vehículos disponibles
    print("Vehículos disponibles:")
    for vehiculo in vehiculos_disponibles:
        disponibilidad = "Disponible" if vehiculo.disponible else "No disponible"
        print(f"{vehiculo.mostrar_info()} - {disponibilidad}")

# Función principal para gestionar la renta de vehículos
def rentar_vehiculo_cliente(cliente):
    mostrar_vehiculos_disponibles()
    seleccion = int(input("Seleccione el número del vehículo que desea rentar: ")) - 1

    if 0 <= seleccion < len(vehiculos_disponibles):
        vehiculo = vehiculos_disponibles[seleccion]
        cliente.rentar_vehiculo(vehiculo)
    else:
        print("Selección inválida.")

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Crear algunos vehículos
    auto1 = Vehiculo("Toyota", "Corolla", 40)
    camion1 = Vehiculo("Volvo", "FMX", 100)
    moto1 = Vehiculo("Yamaha", "R6", 30)

    # Agregar los vehículos al lote
    agregar_vehiculo(auto1)
    agregar_vehiculo(camion1)
    agregar_vehiculo(moto1)

    # Crear un cliente
    cliente1 = Cliente("Juan Perez")

    # Rentar un vehículo
    rentar_vehiculo_cliente(cliente1)

    # Devolver el vehículo
    cliente1.devolver_vehiculo()
