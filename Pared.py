#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def __init__(self):
        pass

    def entrar(self):
        print("Te has chocado con una pared")

    def esPared(self):
        return True

    
