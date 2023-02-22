#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa
from Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self, num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = num

    def __str__(self):
        return f"N {self.norte} | O {self.oeste} | S {self.sur} | E {self.este} | NUM: {self.num}"

    def entrar(self):
        print("Estás en la habitación ", self.num)

    def esHabitacion(self):
        return True

    #Le paso una orientación (Norte(), Sur() etc y un elemento (Pared(), Puerta() etc)).
    #De la orientacion que le he pasado, llamo a su metodo para ponerle el elemento
    def ponerEnElemento(self, unaOrientacion, unEm):
        unaOrientacion.ponerElementoEn(unEm, self)
    