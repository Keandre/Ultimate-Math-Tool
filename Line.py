from math import tan,pi
from fractions import Fraction

class Point:
    x = 0
    y = 0
    def __init__(self,x,y):
        # find the equation
        self.y =  y
        self.x =  x
class Line:

    point1 = (0,0)
    point2 = (0,0)
    midpoint = (0,0)
    slope = Fraction(0)
    angle_radians = 0
    angle_degrees = 0
    length = 0
    equation = ""
    rightBisector = ""
    angle_radians = 0
    angle_degrees = 0

    def __init__(self,point1 = (0,0),point2=(0,0)):
        self.point1 = point1
        self.point2 = point2
        self.midpoint = midpoint()
        self.slope = slope()
        self.length = length()
        self.equation = equation()
        self.rightBisector = rightBisector()
        angle_radians = 0
        angle_degrees = 0


    def midpoint():
        return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)

    def slope():
        return Fraction((point2[1]-point1[1]) / (point2[0]-point1[0]))

    def length():
        return ((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)

    def equation():
        b = point1[1] - slope() * point1[0]

        # Convert to Fraction if it's not a whole number
        b = Fraction(b) if type(b) != int else b

        # Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
        b = "- " + str(b)[1:] if str(b)[0] == "-" else "+ " + str(b)

        return (f"y = {slope()} x {b}")

    def rightBisector():
            # Make slope and make it negative reciporcal
            nume = slope().numerator
            deno = slope().denominator
            negreci_slope = Fraction(-deno, nume)

            b = midpoint()[1] - negreci_slope * midpoint()[0]

            # Convert to Fraction if it's not a whole number
            b = Fraction(b) if int(b) != b else int(b)

            # Make - (-b) into + b
            if type(b) == Fraction:
                b = f'- {b}' if b > 0 else f'+ {str(b)[1:]}'
            else:
                b = f'+ {str(b)[1:]}' if b < 0 else f'+ {b}'

            return (f'y =  {negreci_slope}x {b}')

    def angle_radians():
        return 2*tan(point2[1]-point1[1],point2[0],point1[0])

    def angle_degrees():
        return 2*tan(point2[1]-point1[1],point2[0],point1[0])*180/pi

    def onLine(point = (0,0)):
        b = point1[1] - slope() * point1[0]

        # Convert to Fraction if it's not a whole number
        b = Fraction(b) if type(b) != int else b

        return (point[0]*slope() + b == point[1])




