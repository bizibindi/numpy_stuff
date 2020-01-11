import numpy as np
import cmath as cm

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
    
    
    