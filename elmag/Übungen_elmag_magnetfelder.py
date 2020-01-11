# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 12:20:35 2020

@author: Lucas
"""

import elmag_formelsammlung as elmag

#Seite 108

def proton_im_erdmagnetfeld():
    B = elmag.gauss2tesla(0.6)
    v = 1e7
    q = elmag.elementarladung
    winkel = elmag.np.radians(70)
    
    return elmag.lorentzkraft_betraege(q, v, B, winkel)
