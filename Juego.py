#!/usr/bin/python
#-*- coding: utf-8 -*-

import random

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared
from Bomba import Bomba
from Bicho import Bicho
from Modo import Modo
from Perezoso import Perezoso
from Agresivo import Agresivo

class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = list()

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarHabitacion(self, unNum):
        return Habitacion(unNum) 

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, unaHab, otraHab):
        puerta = Puerta()
        puerta.lado1 = unaHab
        puerta.lado2 = otraHab

        return puerta

    def fabricarBomba(self):
        return Bomba()

    def obtenerHabitacion(self,num):
        return self.laberinto.obtenerHabitacion(num)




    #Agrega un bicho siempre en la primera habitacion
    def agregarBicho(self, unBicho):
        hab = self.obtenerHabitacion(0)
        unBicho.posicion = hab
        self.bichos.append(unBicho)

    #agrega un bicho en una habitación random
    def agregarBichoRandom(self, unBicho):
        habitaciones = self.laberinto.obtenerHabitaciones()
        hab = random.choice(habitaciones)
        unBicho.posicion = hab
        self.bichos.append(unBicho)


    def fabricarModoAgresivo(self):
        return Agresivo()

    def fabricarModoPerezoso(self):
        return Perezoso()


    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho

    def fabricarBichoAgresivoEn(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        bicho.posicion = unaHab
        return bicho


    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 100
        bicho.poder = 0
        return bicho

    def fabricarBichoPerezosoEn(self, unaHab):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 100
        bicho.poder = 0
        bicho.posicion = unaHab
        return bicho


    def laberinto4Habitaciones2Bichos(self):
        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        puerta1_2 = self.fabricarPuerta(hab1,hab2)
        puerta1_3 = self.fabricarPuerta(hab1,hab3)
        puerta2_4 = self.fabricarPuerta(hab2,hab4)
        puerta3_4 = self.fabricarPuerta(hab3,hab4)

        bomba = self.fabricarBomba()
        bomba.component = self.fabricarPared()
        hab1.norte = bomba
        hab1.sur = puerta1_2
        hab1.oeste = self.fabricarPared()
        hab1.este = puerta1_3

        hab2.norte = puerta1_2
        hab2.sur = self.fabricarPared()
        hab2.oeste = self.fabricarPared()
        hab2.este = puerta2_4

        hab3.norte = self.fabricarPared()
        hab3.sur = puerta3_4
        hab3.oeste = puerta1_3
        hab3.este = self.fabricarPared()

        hab4.norte = puerta3_4
        hab4.sur = self.fabricarPared()
        hab4.oeste = puerta2_4
        hab4.este = self.fabricarPared()

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        bicho1 = self.fabricarBichoAgresivoEn(hab1)
        bicho2 = self.fabricarBichoPerezosoEn(hab2)
        bicho3 = self.fabricarBichoAgresivoEn(hab3)
        bicho4 = self.fabricarBichoPerezosoEn(hab4)

        self.bichos.extend([bicho1, bicho2, bicho3, bicho4]) 

    def laberinto2HabitacionesFMD(self):
        self.laberinto = self.fabricarLaberinto()

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1, hab2)

        bm1 = self.fabricarBomba()
        bm1.component = self.fabricarPared()
        hab1.norte = bm1
        hab1.oeste = self.fabricarPared()
        hab1.este = self.fabricarPared()

        bm2 = self.fabricarBomba()
        bm2.component = self.fabricarPared()
        hab2.sur = bm2
        hab2.oeste = self.fabricarPared()
        hab2.este = self.fabricarPared()

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2Habitaciones(self):
        self.laberinto = Laberinto()

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta()
        puerta.lado1 = hab1
        puerta.lado2 = hab2

        hab1.norte = Pared()
        hab1.oeste = Pared()
        hab1.este = Pared()
        hab1.sur = puerta

        hab2.sur = Pared()
        hab2.oeste = Pared()
        hab2.este = Pared()
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

juego = Juego()
juego.laberinto4Habitaciones2Bichos()

print("--ESTO ES PARA PROBAR--")

for i in juego.laberinto.habitaciones:
    print(i)

for i in juego.bichos:
    print(i)

hab1 = juego.obtenerHabitacion(0)
hab2 = juego.obtenerHabitacion(1)
hab3 = juego.obtenerHabitacion(2)
hab4 = juego.obtenerHabitacion(3)

print()
print("--Intentando pasar de la hab. 1 a la hab. 2--")
hab1.sur.entrar()
print("--Abro puerta--")
hab1.sur.abrirPuerta()
print("--Intentando pasar de la hab. 1 a la hab. 2--")
hab1.sur.entrar()

print()
hab1.norte.entrar()
hab1.norte.activarBomba()
hab1.norte.entrar()
hab1.norte.entrar()
