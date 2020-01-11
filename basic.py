import numpy as np
import cmath
from fractions import Fraction

def mitternacht(a, b, c):
    r = cmath.sqrt(np.square(b)-4 * a * c)
    
    return (-b + r)/(2*a),(-b - r)/(2*a)



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