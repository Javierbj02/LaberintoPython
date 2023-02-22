#!/usr/bin/python
#-*- coding: utf-8 -*-

class ElementoMapa:
    def __init__(self):
        self.padre = None

    def entrar(self):
        pass

    def esBomba(self):
        return True

    def esHabitacion(self):
        return False

    def esPared(self):
        return False

    def esPuerta(self):
        return False

