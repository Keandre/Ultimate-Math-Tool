from math import pi, radians, sqrt, tan
import decimal
from fractions import Fraction
# ---------------Area/Perimeters------------------------------

#Regular Polygons
def perimeterRegularPolygons(numOfSides,sideLength):
  return numOfSides*sideLength

def areaRegularPolygons(numOfSides,sideLength):
  apothem = sideLength/decimal((2*tan(radians(180/numOfSides))))
  return ((apothem*perimeterRegularPolygons(numOfSides,sideLength))/2)

# Circle
def areaOfCircle(radius):
    return pi * radius ** 2


def perimeterOfCircle(radius):
    return pi * radius * 2

# Triangle
def areaOfTriangle(base, height):
    return (base * height) / 2


def perimeterOfTriangle(a, b, c):
    return a + b + c

# Rectangle

def areaOfRectangle(length, width):
    return length * width


def perimeterOfRectangle(length, width):
    return (length * 2) + (width * 2)

#Trapezoid

def areaOfTrapezoid(a,b,h):
    return (a+b)/2 * h

def perimeterOfTrapezoid(a,b,c,d):
    return a+b+c+d


# Do parallelogram, trapezoid

# ------------------------------Lines and Stuff----------------------
def midpoint(x1,y1,x2,y2):
  return ((x1+x2)/2,(y1+y2)/2)

def slope(y2, y1, x2, x1):
    try:
        return Fraction((y2 - y1)/ (x2 - x1))
    except ZeroDivisionError:
        return 0

#Returns the square root (√) of...
def lengthOfLine(x1, y1, x2, y2):
    return (y2 - y1)**2 + (x2 - x1)**2

def linearEquation(x1, y1, x2, y2):
    b = y1 - slope(y2, y1, x2, x1) * x1

    # Convert to Fraction if it's not a whole number
    b = Fraction(b) if type(b) != int else b

    # Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
    b = "- " + str(b)[1:] if str(b)[0] == "-" else "+ " + str(b)

    return (f"y = {slope(y2,y1,x2,x1)} x {b}")

def rightBisector(x1, y1, x2, y2):
    midpoint = midpoint(x1,y1,x2,y2)

    # Make slope and make it negative reciporcal
    slope_frac = slope(y2, y1, x2, x1)
    nume = slope_frac.numerator
    deno = slope_frac.denominator
    negreci_slope = Fraction(-deno, nume)

    b = midpoint[1] - negreci_slope * midpoint[0]

    # Convert to Fraction if it's not a whole number
    b = Fraction(b) if int(b) != b else int(b)

    # Make - (-b) into + b
    if type(b) == Fraction:
        b = f'- {b}' if b > 0 else f'+ {str(b)[1:]}'
    else:
        b = f'+ {str(b)[1:]}' if b < 0 else f'+ {b}'

    return (f'y =  {negreci_slope}x {b}')

# ------------------------------------------------------------------------------
