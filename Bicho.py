#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bicho:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.modo = None
        self.posicion = None

    def __str__(self):
        return f"BICHO: posición: {self.posicion.num} | modo: {self.modo} | vida: {self.vidas} | daño: {self.poder}"

