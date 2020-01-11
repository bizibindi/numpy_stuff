# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:32:27 2020

@author: Lucas
"""

import sys
sys.path.append("..")

import numpy as np
import basic_arithmetic.basic as basic
"""
Einheiten
Magnetfeld B -> Tesla [(N/C)/(m/s) = N/(A*m)]
                1  Tesla = 10^4 Gauss
"""

"""
Konstanten
"""
elementarladung = 1.6022e-19
masse_proton = 1.67e-27

"""
Formeln
"""

def tesla2gauss(t):
    """
    Umwandlung Telsa zu Gauss
    """
    
    g = t*1e-4
    return g

def gauss2tesla(g):
    """
    Umwandlung Gauss zu Telsa
    """
    
    t = g*1e4
    return t

def lorentzkraft(q,v_v, B_v):
    """
    Berechnet Lorentzkraft
    q = Ladung
    v_v = geschwindigkeits_vektor
    B_v = Magnetfeld_vektor
    
    Gibt Lorenzkraft als Vektor zurück
    """
    
    F_v = np.cross((q*v_v),B_v)
    
    return F_v

def lorentzkraft_betraege(q, v, B, sigma):
    """
    Berechnet Betrag Lorentzkraft
    q = Ladung
    v = Betrag der Geschwindigkeit
    B = Betrag des Magnetfeldes
    sigma = Zwischenwinkel Geschwindigkeits-Vektor und
    Magnetfeld-Vektor
    
    Gibt Lorenzkraft als Betrag zurück
    """
    
    F = q * v * B * basic.sinus(sigma)
    
    return F

def strom_durch_leiterstück(q,n, A, vd):
    """
    q = Ladung
    n = Ladungsdichte
    A = Querschnittsfläche des Leitersstückes
    vd = Driftgeschwindigkeit
    
    Gibt Strom durch Leiterstück zurück
    """
    
    I = q * n * A * vd
    
    return I

def lorentzkraft_durch_stromdurchflossenen_leiter(I, l_v, B_v):
    """
    I = Strom durch Leiter
    l_v = in Stromrichtung ausgerichteter Vektor
    B = Magnetfeld als Vektor
    """
    
    F_l_v = np.cross((I*l_v), B_v)
    
    return F_l_v

def lorentzkraft_durch_stromdurchflossenen_leiter_betrag(I, l, B, winkel):
    """
    I = Strom durch Leiter
    l_v = in Stromrichtung ausgerichteter Vektor
    B = Magnetfeld als Vektor
    """
    
    F_l = I * l * B * basic.sinus(winkel)
    
    return F_l

def kreisradius_ladung_mit_magnetfeld_senkrecht_zur_bewegungsrichtung(q, B, m, v):
    """
    q = Ladung
    B = Magnetfeldstaerke
    m = Masse
    v = Geschwindigkeit
    
    Gibt den Kreisradius des Kreises zurück welcher sich durch eine Ladung ergibt,
    deren Bewegungsrichtung senkrecht zum Magnetfeld liegt.
    """
    
    r = (m*v)/(q*B)
    
    return r

def Zyklotronfrequenz(q, B, m):
    """
    q = Ladung
    B = Magnetfeldstaerke
    m = Masse
    
    Gibt die Frequenz der Kreisbeweung der Ladung in einem senkrecht zur
    Bewgungsrichtung liegendem Magnetfeld.
    """
    
    T = (2*np.pi*m)/(q*B)
    f = 1/T
    
    return f






