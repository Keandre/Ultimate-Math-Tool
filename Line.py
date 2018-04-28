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

    def __init__(self,point1 = (0,0),point2=(0,0)):
        self.point1 = point1
        self.point2 = point2

    @property
    def midpoint(self):
        return ((self.point1[0]+self.point2[0])/2,(self.point1[1]+self.point2[1])/2)

    @property
    def slope(self):
        try:
            return Fraction((self.point2[1]-self.point1[1]) / (self.point2[0]-self.point1[0]))
        except ZeroDivisionError:
            return 0

    @property
    def length(self):
        return ((self.point2[0]-self.point1[0])**2+(self.point2[1]-self.point1[1])**2)

    @property
    def equation(self):
        b = self.point1[1] - self.slope() * self.point1[0]

        # Convert to Fraction if it's not a whole number
        b = Fraction(b) if type(b) != int else b

        # Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
        b = "- " + str(b)[1:] if str(b)[0] == "-" else "+ " + str(b)

        return (f"y = {self.slope()} x {b}")

    @property
    def rightBisector(self):
            # Make slope and make it negative reciporcal
            nume = self.slope().numerator
            deno = self.slope().denominator
            negreci_slope = Fraction(-deno, nume)

            b = self.midpoint()[1] - negreci_slope * self.midpoint()[0]

            # Convert to Fraction if it's not a whole number
            b = Fraction(b) if int(b) != b else int(b)

            # Make - (-b) into + b
            if type(b) == Fraction:
                b = f'- {b}' if b > 0 else f'+ {str(b)[1:]}'
            else:
                b = f'+ {str(b)[1:]}' if b < 0 else f'+ {b}'

            return (f'y =  {negreci_slope}x {b}')

    @property
    def angle_radians(self):
        return 2*tan(self.point2[1]-self.point1[1],self.point2[0],self.point1[0])

    @property
    def angle_degrees(self):
        return 2*tan(self.point2[1]-self.point1[1],self.point2[0],self.point1[0])*180/pi

    def onLine(self, point=(0, 0)):
        b = self.point1[1] - self.slope() * self.point1[0]

        # Convert to Fraction if it's not a whole number
        b = Fraction(b) if type(b) != int else b

        return (self.point[0] * self.slope() + b == self.point[1])
