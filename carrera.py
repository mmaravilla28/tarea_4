#Se importan las librerias utilizadas
import math
import random

class Vehiculo:
    #se definen las variables para la distancia total y la cantidad de ciclos utilizados por lo vehículos
    meta = 1000
    cantidad_ciclos = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False
        self.recorrido = 0
        self.fuerza = 0

    def __repr__(self):
        return self.nombre

    def calcular_fuerza(self):
        return random.uniform(0, 9)

    def comprobar_meta(self):
        self.estado =  Vehiculo.meta < self.recorrido
        return self.estado

    def avanzar(self, fuerza_motor):
        if not self.comprobar_meta():
            self.fuerza = self.calcular_fuerza()
            self.recorrido +=  math.ceil(fuerza_motor(self.fuerza))
            Vehiculo.cantidad_ciclos += 1
        return self.comprobar_meta()

#se crean las clases para cada vehículo que compite
class Camion(Vehiculo):
    def __init__(self):
        super(Camion, self).__init__(nombre = 'Camion')

    def avanzar(self):
        return super(Camion, self).avanzar(fuerza_motor = lambda x: 2 * x + 1)

class Tractor(Vehiculo):
    def __init__(self):
        super(Tractor, self).__init__(nombre = 'Tractor')

    def avanzar(self):
        return super(Tractor, self).avanzar(fuerza_motor = math.log2)

class Sedan(Vehiculo):
    def __init__(self):
        super(Sedan, self).__init__(nombre = 'Sedan')

    def avanzar(self):
        return super(Sedan, self).avanzar(fuerza_motor = lambda x: 3 * x**2)

class Bus(Vehiculo):
    def __init__(self):
        super(Bus, self).__init__(nombre = 'Bus')

    def avanzar(self):
        return super(Bus, self).avanzar(fuerza_motor = lambda x: 5*x)

#se instancias las clases para cada vehículo
camion = Camion()
tractor = Tractor()
sedan = Sedan()
bus = Bus()

#se crea la lista de los vehículos
lista_vehiculos = [camion, tractor, sedan, bus]

#se imprime le recorrido para cada vehículo
while not any([i.avanzar() for i in lista_vehiculos]):
    print([(i.nombre, i.recorrido) for i in lista_vehiculos])

#se imprime el resultado final del ganador y los ciclos utilizados en total
print('\nEl vehículo ganador es:', [(i.nombre, 'con una distancia total recorrida de: ' , i.recorrido) for i in lista_vehiculos if i.estado])
print('\nSe utilizaron:' , Vehiculo.cantidad_ciclos, 'ciclos en total')

pass