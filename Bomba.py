#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False

    def __str__(self):
        return f"{self.component} con bomba"

    def esBomba(self):
        return True

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado")
            self.activa = False
        else:
            super().entrar()

    def activarBomba(self):
        self.activa = True