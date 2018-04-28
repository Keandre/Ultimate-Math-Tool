from math import atan2,pi
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
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        midpoint_x = (point1_x + point2_x) / 2
        midpoint_y = (point1_y + point2_y) / 2
        return midpoint_x, midpoint_y

    @property
    def slope(self):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        try:
            return Fraction((point2_y-point1_y) / (point2_x-point1_x))
        except ZeroDivisionError:
            return 0

    @property
    def length(self):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        return ((point2_x-point1_x)**2+(point2_y-point1_y)**2)

    @property
    def equation(self):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        b = point1_y - self.slope * point1_x

        # Convert to Fraction if it's not a whole number
        if b.is_integer():
            b = int(b)
        else:
            b = Fraction(b)

        # Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
        b = "- " + str(b)[1:] if str(b)[0] == "-" else "+ " + str(b)

        return (f"y = {self.slope} x {b}")

    @property
    def rightBisector(self):
            # Make slope and make it negative reciporcal
            nume = self.slope.numerator
            deno = self.slope.denominator
            negreci_slope = Fraction(-deno, nume)

            b = self.midpoint[1] - negreci_slope * self.midpoint[0]

            # Convert to Fraction if it's not a whole number
            if b.is_integer():
                b = int(b)
            else:
                b = Fraction(b)

            # Make - (-b) into + b
            if type(b) == Fraction:
                b = f'- {b}' if b > 0 else f'+ {str(b)[1:]}'
            else:
                b = f'+ {str(b)[1:]}' if b < 0 else f'+ {b}'

            return (f'y =  {negreci_slope}x {b}')

    @property
    def angle_radians(self):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        return atan2(point2_y-point1_y,point2_x-point1_x)

    @property
    def angle_degrees(self):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        return atan2(point2_y-point1_y,point2_x-point1_x)*180/pi

    def onLine(self, point=(0, 0)):
        point1_x, point1_y = self.point1
        point2_x, point2_y = self.point2
        b = point1_y - self.slope * point1_x

        # Convert to Fraction if it's not a whole number
        if b.is_integer():
            b = int(b)
        else:
            b = Fraction(b)

        return (point[0] * self.slope + b == point[1])
