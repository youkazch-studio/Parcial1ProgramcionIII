class Paciente:
    def __init__(self, nombre, motivo_consul):
        self.nombre = nombre
        self.motivo_consul = motivo_consul
        self.tcita= False

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.sala_espera = []
        self.doctores = ['Dra. Montano', 'Dra. Juarez', 'Dr. Arias']
        self.doctor_index = 0  # Sirve para asignar un doctor por cada paciente de manera rotativa

    def registrar_paciente(self, paciente):
        if paciente.tcita:
            self.sala_espera.append(paciente)
            print(f"{paciente.nombre} Ya cuenta una cita. Redirigiendo a la sala de espera.")
        else:
            paciente.tcita = True
            self.pacientes.append(paciente)
            doctor_asignado = self.doctores[self.doctor_index]
            self.doctor_index = (self.doctor_index + 1) % len(self.doctores)
            print(f"Cita creada para {paciente.nombre} con {doctor_asignado}.")

    def mostrar_sala_espera(self):
        print("Pacientes en sala de espera:")
        for paciente in self.sala_espera:
            print(f"- {paciente.nombre}, Motivo: {paciente.motivo_consul}")

# Ejemplo:
consultorio = Consultorio()

paciente1 = Paciente("Jack", "Calentura")
paciente2 = Paciente("Daniel", "Dolor de garganta")

consultorio.registrar_paciente(paciente1)
consultorio.registrar_paciente(paciente1)  # Segunda vez que llega, va a sala de espera
consultorio.registrar_paciente(paciente2)

consultorio.mostrar_sala_espera()