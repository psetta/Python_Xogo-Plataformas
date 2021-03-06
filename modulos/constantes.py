# -*- coding: utf-8 -*-

from __future__ import division

import pygame

def simplificar_fraccion(dividendo, divisor):
        for i in range(dividendo,2,-1):
            if dividendo%i == 0 and divisor%i == 0:
                    return dividendo/i, divisor/i
        return None

#CONSTANTES

pygame.display.init()

FPS = 60

RESOLUCION = [pygame.display.Info().current_w,pygame.display.Info().current_h]

RESOLUCION = 800,500

ANCHO_VENTANA, ALTO_VENTANA = RESOLUCION

ASPECTRO = RESOLUCION[0]/RESOLUCION[1]
ASPECTRO_P =  simplificar_fraccion(*RESOLUCION)

DIF_ASP = 1.3333

DIMENSIONS_GL = 150
DIMENSIONS_GL_ESTANDAR = DIMENSIONS_GL*DIF_ASP

ANCHO_PANTALLA_GL_PRO = DIMENSIONS_GL*ASPECTRO
ALTO_PANTALLA_GL_PRO = DIMENSIONS_GL

ANCHO_CADRO = 5
ALTO_CADRO = 5

MARCO_LATERAL = int(ANCHO_VENTANA - ((DIMENSIONS_GL_ESTANDAR*ANCHO_VENTANA)/ANCHO_PANTALLA_GL_PRO))

if MARCO_LATERAL < 0:
    MARCO_VERTICAL = int(abs(MARCO_LATERAL)/DIF_ASP)
else:
    MARCO_VERTICAL = 0

MARCO_LATERAL = max(0,MARCO_LATERAL)
MARCO_VERTICAL = max(0,MARCO_VERTICAL)

ANCHO_PANTALLA_GL = DIMENSIONS_GL_ESTANDAR
ALTO_PANTALLA_GL = DIMENSIONS_GL

COLOR_LIMPIADO = [1,1,1,1]

#CAMBIARAN DESPOIS:

pos_camara = [0,0]

lista_cadros_colision = []
lista_vertices_cadros_colision = []
vertices_cadricula = []

ANCHO_FASE = 0
ALTO_FASE = 0