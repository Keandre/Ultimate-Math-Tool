from math import pi 
from math import sqrt
from fractions import Fraction 

#---------------Area/Perimeters------------------------------

#Circle
def areaOfCircle(radius):
  return pi*radius**2
  
def perimeterOfCircle(radius):
  return math.pi*radius*2

#Square
def areaOfSquare(side):
  return side**2 
  
def perimeterOfSquare(side):
  return side*4
  
#Triangle
def areaOfTriangle(base,height):
  return base*height 

def perimeterOfTriangle(a,b,c):
  return a+b+c

#Rectangle

def areaOfRectangle(length,width):
  return length*width
  
def perimeterOfRectangle(length,width):
  return (length*2)+(width*2)

#Do parallelogram, trapezoid

#------------------------------Lines and Stuff----------------------

def slope(y2,y1,x2,x1):
  return Fraction(y2-y1,x2-x1)
  
def lengthOfLine(x1,y1,x2,y2):
  return ("√",math.sqrt(y2-y1)+math.sqrt(x2-x1))
  
def linearEquation(x1,y1,x2,y2):
  b = y1 - slope(y2,y1,x2,x1)*x1
  
  #Convert to Fraction if it's not a whole number
  b = Fraction(b) if type(b) != int else b 
  
  #Change to '+Fraction' if it's a negative number and '-Fraction' if it's a positive one.
  b = "+ " + str(b)[1:] if str(b)[0]=="-" else "- " + b 
  
  return ("y = "+str(Fraction(y2-y1,x2-x1))+"x " + b)
  
def rightBisector(x1,y1,x2,y2):
  midpoint = [(x1+x2)/2,(y1+y2)/2]
  
  #Make slope and make it negative reciporcal 
  slope_frac = slope(y2,y1,x2,x1)
  nume = slope_frac.numerator
  deno = slope_frac.denominator 
  negreci_slope = Fraction(-deno,nume)
  
  b = midpoint[1] - negreci_slope*midpoint[0]
  
  #Convert to Fraction if it's not a whole number
  b = Fraction(b) if int(b) != b else int(b) 
  
  #Make - (-b) into + b 
  if type(b)==Fraction:
    b = f'- {b}' if b >= 0 else f'+ {str(b)[1:]}'
  else:
    b = f'+ {str(b)[1:]}' if b <0 else f'+ {b}'
    
  

  return (f'y =  {negreci_slope}x {b}')
  
#------------------------------------------------------------------------------
  
