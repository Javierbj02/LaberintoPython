#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Decorator(ElementoMapa):
    
    def __init__(self):
        self.component = None

    def entrar(self):
        self.component.entrar()