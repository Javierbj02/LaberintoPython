#!/usr/bin/python
#-*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Bomba import Bomba

class Juego:
    def __init__(self):
        self.laberinto = None

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarHabitacion(self, unNum):
        return Habitacion(unNum) 

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, unaHab, otraHab):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab

        return puerta

    def fabricarBomba(self):
        return Bomba()

    def obtenerHabitacion(self,num):
        return self.laberinto.obtenerHabitacion(num)

    def laberinto2HabitacionesFMD(self):
        #TODO
        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1, hab2)

        bm1 = self.fabricarBomba()
        bm1.component = self.fabricarPared()
        hab1.norte = self.fabricarPared()
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()

        bm2 = self.fabricarBomba()
        bm2.component = self.fabricarPared()
        hab2.sur = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2Habitaciones(self):
        self.laberinto = Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.norte = Pared()
        hab1.oeste = Pared()
        hab1.este = Pared()
        hab1.sur = puerta

        hab2.sur = Pared()
        hab2.oeste = Pared()
        hab2.este = Pared()
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

juego = Juego()
juego.laberinto2HabitacionesFMD()

