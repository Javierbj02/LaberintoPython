#!/usr/bin/python
#-*- coding: utf-8 -*-

class Laberinto:
    def __init__(self):
        self.habitaciones = list()

    def agregarHabitacion(self, hab):
        self.habitaciones.append(hab)

    def obtenerHabitacion(self, num):
        return self.habitaciones[num]

    def obtenerHabitaciones(self):
        return self.habitaciones