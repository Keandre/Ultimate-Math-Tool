"""
The Ultimate Math Tool by FanFreak247 & DiracDelta
Written in Python 3.6.5
Copyright © FanFreak247 2018.
This code is not to be used, redistributed or copied without the author's permission.
"""
from math import pi, radians, sqrt, tan
import decimal
from fractions import Fraction
# ---------------Area/Perimeters------------------------------


def perimeterRegularPolygons(numOfSides,sideLength):
  return numOfSides*sideLength

def areaRegularPolygons(numOfSides,sideLength):
  apothem = sideLength/decimal((2*tan(radians(180/numOfSides))))
  return ((apothem*perimeterRegularPolygons(numOfSides,sideLength))/2)


def areaOfCircle(radius):
    return pi * radius ** 2


def perimeterOfCircle(radius):
    return pi * radius * 2


def areaOfTriangle(base, height):
    return (base * height) / 2


def perimeterOfTriangle(a, b, c):
    return a + b + c


def areaOfRectangle(length, width):
    return length * width


def perimeterOfRectangle(length, width):
    return (length * 2) + (width * 2)


def areaOfTrapezoid(a,b,h):
    return (a+b)/2 * h

def perimeterOfTrapezoid(a,b,c,d):
    return a+b+c+d

# ------------------------------------------------------------------------------
