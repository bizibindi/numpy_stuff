# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:20:35 2020

@author: Lucas
"""

import sys
sys.path.append("..")

import numpy as np
import elmag_formelsammlung as elmag
import basic_arithmetic.basic as basic

def proton_im_erdmagnetfeld():
    """
    Seite 105
    """
    B = elmag.gauss2tesla(0.6)
    v = 1e7
    q = elmag.elementarladung
    winkel = np.radians(70)
    
    F_l = elmag.lorentzkraft_betraege(q, v, B, winkel)
    
    print(F_l)

def drahtstueck_im_magnetfeld():
    """
    Seite 108
    """
    
    l = 3e-3
    I = 3
    B = 0.02
    winkel = np.radians(30)
    
    print(elmag.lorentzkraft_durch_stromdurchflossenen_leiter_betrag(I, l, B, winkel))
