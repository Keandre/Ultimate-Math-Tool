from math import pi
from math import sqrt
from fractions import Fraction
from decimal import Decimal


# ---------------Area/Perimeters-----------------------------------------------------------------------------------------------------------------------------

#------------------------------
#2D SHAPES 2D SHAPES 2D SHAPES
#----------------------------

# Circle
def areaOfCircle(radius):
    return math.pi * (radius ^ 2)


def perimeterOfCircle(radius):
    return math.pi * radius * 2


# Square
def areaOfSquare(side):
    return side ^ 2


def perimeterOfSquare(side):
    return side * 4


# Triangle
def areaOfTriangle(base, height):
    return base * height


def perimeterOfTriangle(a, b, c):
    return a + b + c


# Rectangle

def areaOfRectangle(length, width):
    return length * width


def perimeterOfRectangle(length, width):
    return (length * 2) + (width * 2)

#Parallelogram
def areaofParallelogram(base,height):
    return base*height

def perimeterOfParallelogram(b,a):
    return 2*(a+b)

#Trapezoid
def areaOfTrapezoid(a,b,h):
    return ((a+b)/2)*h

def perimeterOfTrapezoid(a,b,c,d):
    return a+b+c+d

#Pentagon
def areaOfPentagon(a):
    return (1/4)*math.sqrt(5+2*math.sqrt(5))*(a**2)

def perimeterOfPentagon(a,b,c,d,e,):
    return a+b+c+d+e

#Hexagon

def areaOfHexagon(a):
    return (3*math.sqrt(3))*0.5*(a**2)

def perimeterOfHexagon(a):
    return 6*a

#-----------------------------------
# 3D SHAPES 3D SHAPES
#-------------------------------------

def rectangularPrismVolume(l,w,h):
    return l*w*h



# Do parallelogram, trapezoid

# ------------------------------Lines and Stuff-------------------------------------------------------------------------------------------------------------------

def slope(y2, y1, x2, x1):
    return Fraction(y2 - y1, x2 - x1)


def lengthOfLine(x1, y1, x2, y2):
    return ("√", (x1-x2)**2+(y1-y2)**2)


def linearEquation(x1, y1, x2, y2):
    b = y1 - slope(y2, y1, x2, x1) * x1

    # Convert to Fraction if it's not a whole number
    b = Fraction(b) if type(b) != int else b

    # Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
    b = "+ " + str(b)[1:] if str(b)[0] == "-" else "- " + b

    return ("y = " + str(Fraction(y2 - y1, x2 - x1)) + "x " + b)


def rightBisector(x1, y1, x2, y2):
    midpoint = [Fraction(Decimal(str(x1)) + Decimal(str(x2))) / 2, Fraction(Decimal(str(y1)) + Decimal(str(y2))) / 2]

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
        b = f'+ {b}' if b >= 0 else f'- {str(b)[1:]}'
    else:
        b = f'+ {str(b)[1:]}' if b < 0 else f'+ {b}'

    return (f'y =  {negreci_slope}x {b}')

# --------------------------------------------------------------------------------------------------------------------------------------------

