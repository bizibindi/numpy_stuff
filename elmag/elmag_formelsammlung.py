# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:32:27 2020

@author: Lucas
"""

import numpy as np
from .. import basic

"""
Einheiten
Magnetfeld B -> Tesla [(N/C)/(m/s) = N/(A*m)]
                1  Tesla = 10^4 Gauss
"""

"""
Konstanten
"""
elementarladung = 1.6022e-19


"""
Formeln
"""

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
    return q * v * B * basic.sinus(sigma)
 
def tesla2gauss(t):
    """
    Umwandlung Telsa zu Gauss
    """
    return t*1e-4

def gauss2tesla(g):
    """
    Umwandlung Gauss zu Telsa
    """
    return g*1e4





