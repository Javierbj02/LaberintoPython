#!/usr/bin/python
#-*- coding: utf-8 -*-

from Orientacion import Orientacion

class Este(Orientacion):

	def __init__(self):
		pass

	def ponerElementoEn(self, unEm, unaHab):
		unaHab.este = unEm	