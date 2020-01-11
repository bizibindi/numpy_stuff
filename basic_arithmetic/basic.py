import numpy as np
import cmath as cm
import math
def mitternacht(a, b, c):
    r = cm.sqrt(np.square(b)-4 * a * c)
    
    return (-b + r)/(2*a),(-b - r)/(2*a)


def check_val_trig(v):
    """
    Da PI nur angenährt wird kommt man nie ganz auf Null.
    Deshalb muss überprüfft werden ob Wert einer
    trigonometrischen Funktion unter einem Wert liegt.
    """
    if v > 1.22465e-16:
        return v
    
    return 0


def sinus(winkel):
    """
    Damit Sinus von pi auch 0 gibt und nicht eine
    sehr kleine Zahl.
    """
    
    return check_val_trig(np.sin(winkel))


def cosinus(winkel):
    """
    Damit Cosinus von pi/2 auch 0 gibt und nicht eine
    sehr kleine Zahl.
    """
    return check_val_trig(np.cos(winkel))
    
    
def toVector(betrag, winkel):
    """
    Umwandlung von Betrag und Winkel in einen xy-Vektor.
    """
    return np.array([betrag*sinus(winkel), betrag*cosinus(winkel)])


def eng_string( x, format='%s', si=False):
    '''
    Returns float/int value <x> formatted in a simplified engineering format -
    using an exponent that is a multiple of 3.

    format: printf-style string used to format the value before the exponent.

    si: if true, use SI suffix for exponent, e.g. k instead of e3, n instead of
    e-9 etc.

    E.g. with format='%.2f':
        1.23e-08 => 12.30e-9
             123 => 123.00
          1230.0 => 1.23e3
      -1230000.0 => -1.23e6

    and with si=True:
          1230.0 => 1.23k
      -1230000.0 => -1.23M
    '''
    sign = ''
    if x < 0:
        x = -x
        sign = '-'
    exp = int( math.floor( math.log10( x)))
    exp3 = exp - ( exp % 3)
    x3 = x / ( 10 ** exp3)

    if si and exp3 >= -24 and exp3 <= 24 and exp3 != 0:
        exp3_text = 'yzafpnum kMGTPEZY'[ ( exp3 - (-24)) / 3]
    elif exp3 == 0:
        exp3_text = ''
    else:
        exp3_text = 'e%s' % exp3

    return ( '%s'+format+'%s') % ( sign, x3, exp3_text)
    
def printeng(v):
    print(eng_string(v))
    