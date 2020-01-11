# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:32:27 2020

@author: Lucas
"""

"""
Einheiten
Magnetfeld B -> Tesla [(N/C)/(m/s) = N/(A*m)]
                1  Tesla = 10^4 Gauss
"""

import numpy as np

"""
Konstanten
"""
elementarladung = 1.6022e-19

def sinus(angle):
    """
    Damit Sinus von pi auch 0 gibt und nicht eine
    sehr kleine Zahl.
    """
    val = np.sin(angle)
    if val > 1.22465e-16:
        return val
    else:
        return 0
    
def lorentzkraft(q,v_v, B_v):
    
    """
    Berechnet Lorentzkraft
    q = Ladung
    v_v = geschwindigkeits_vektor
    B_v = Magnetfeld_vektor
    """
    return np.cross((q*v_v),B_v)

def lorentzkraft_betraege(q, v, B, sigma):
    """
    Berechnet Betrag Lorentzkraft
    q = Ladung
    v = Betrag der Geschwindigkeit
    B = Betrag des Magnetfeldes
    sigma = Zwischenwinkel Geschwindigkeits-Vektor und
    Magnetfeld-Vektor
    """
    return q * v * B * sinus(sigma)
 
def tesla2gauss(t):
    return t*1e-4

def gauss2tesla(g):
    return g*1e4





