#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = num

    def entrar(self):
        print("Estás en la habitación ", self.num)

    def esHabitacion(self):
        return True

    