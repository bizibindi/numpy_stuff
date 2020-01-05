from numpy import *
import cmath
from fractions import Fraction

def mitternacht(a, b, c):
    r = cmath.sqrt(square(b)-4 * a * c)
    
    return (-b + r)/(2*a),(-b - r)/(2*a)

def bruch(val):
    for v in val:
        print(str(Fraction(v.real)) + " j" + str(Fraction(v.imag)))

#print(bruch(mitternacht(1,1,1)))


