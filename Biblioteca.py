from datetime import datetime, timedelta

class Lector:
    def __init__(self, nombre, id_tarjeta):
        self.nombre = nombre
        self.id_tarjeta = id_tarjeta   

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.fecha_prestamo = None
        self.fecha_devolucion = None

class Biblioteca:
    def __init__(self):
        self.prestamos = {}
        self.historial = []

    def prestar_libro(self, lector, libro):
        fecha_actual = datetime.now()
        fecha_limite = fecha_actual + timedelta(days=20)  # el lapso de tiempo es 20 días de préstamo
        libro.fecha_prestamo = fecha_actual
        libro.fecha_devolucion = fecha_limite
        if lector.id_tarjeta not in self.prestamos:
            self.prestamos[lector.id_tarjeta] = []
        self.prestamos[lector.id_tarjeta].append(libro)
        self.historial.append((lector.nombre, libro.titulo, fecha_actual, fecha_limite))
        print(f"Libro '{libro.titulo}' prestado a {lector.nombre} hasta el {fecha_limite}.")

    def devolver_libro(self, lector, libro):
        libros_prestados = self.prestamos.get(lector.id_tarjeta, [])
        if libro in libros_prestados:
            fecha_actual = datetime.now()
            if fecha_actual > libro.fecha_devolucion:
                print(f"Devolución tardía de '{libro.titulo}'. Sanción aplicada.")
            else:
                print(f"Libro '{libro.titulo}' devuelto a tiempo.")
            libros_prestados.remove(libro)
            if not libros_prestados:
                del self.prestamos[lector.id_tarjeta]
        else:
            print(f"{lector.nombre} no tiene el libro '{libro.titulo}' prestado.")

    def mostrar_historial(self):
        print("Historial de préstamos:")
        for registro in self.historial:
            print(f"Lector: {registro[0]}, Libro: {registro[1]}, Fecha de préstamo: {registro[2]}, Fecha de devolución: {registro[3]}")

# Ejemplo:
biblioteca = Biblioteca()

lector1 = Lector("Melissa Arias", "77777")
libro1 = Libro("El Principito")
libro2 = Libro("la mecanica del corazon")

biblioteca.prestar_libro(lector1, libro1)
biblioteca.prestar_libro(lector1, libro2)
biblioteca.devolver_libro(lector1, libro1)
biblioteca.mostrar_historial()