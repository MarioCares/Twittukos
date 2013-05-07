#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Mario Cares <mcares@puertosolutions.cl'

from Ventanas.Principal import Class_Principal

try:
    with open('config/Credenciales.json'): pass
except IOError:
    print 'Credenciales no existen ! Cargando Autorizacion'
    from Ventanas.Autentificacion import Class_Autentificacion
    ventana = Class_Autentificacion()
    ventana.mostrar()

print 'Mostrando ventana principal'
principal = Class_Principal()
principal.mostrar()