"""
The Ultimate Math Tool by FanFreak247 & DiracDelta
Written in Python 3.6.5
Copyright © FanFreak247 2018.
This code is not to be used, redistributed or copied without the author's permission.
"""
from numpy import linalg
from numpy import array
from math import sqrt

class NoRootsError(Exception):
    pass
class NoRationalNumbersError(Exception):
    pass
class NotQuadraticError(Exception):
    pass

def returnX(a,b,c):
  if a==0:
    raise NotQuadraticError
  if b**2-4*a*c < 0:
    raise NoRootsError
  try:
    first_solution = (-b + sqrt(b**2-4*a*c))/2*a
    second_solution = (-b - sqrt(b**2-4*a*c))/2*a
    return (first_solution,second_solution)
  except ValueError:
    raise NoRationalNumbersError

#Currently in development.
