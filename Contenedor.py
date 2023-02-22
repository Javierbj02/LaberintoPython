#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):

	def __init__(self):
		self.hijos = list()

	def agregarHijos(self, unHijo):
		unHijo.padre = self
		self.hijos.append(unHijo)




