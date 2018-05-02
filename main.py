"""
The Ultimate Math Tool by FanFreak247 & DiracDelta
Written in Python 3.6.5
Copyright © FanFreak247 2018.
This code is not to be used, redistributed or copied without the author's permission.
"""

import Geometry
import Algebra
from Line import Line

print("Welcome to the Ultimate Math Tool. What would you like to do?\n")
while True:
    choice = input("1 - Area\n2 - Perimeter\n3 - Lines and Stuff\n4 - Exit")
    if choice == "1":
        while True:
            choice = input("What would you like to calculate the area of?\n 1 - Regular Polygons\n 2 - Triangle\n 3 - Rectangle\n 4 - Trapezoid\n")
            #Reg Polygons
            if choice == "1":
                numOfSides = float(input("Enter in the amount of sides."))
                sideLength = float(input("Enter in the side length."))
                print(f'The area is: {Geometry.areaRegularPolygons(numOfSides,sideLength)}\n')
            #Triangle
            if choice == "2":
                base = float(input("Enter in the base length of the triangle."))
                height = float(input("Enter in the height of the triangle."))
                print(f'The area of the triangle is: {Geometry.areaOfTriangle(base,height)}\n')
            #Rectangle
            if choice == "3":
                length = float(input("Please enter the length of the rectangle."))
                width = float(input("Please enter the width."))
                print(f'The area of the rectangle is: {Geometry.areaOfRectangle(length,width)}\n')
            #Trapezoid
            if choice == "4":
                a = float(input("Please enter the a of the trapezoid."))
                b = float(input("Please enter the b of the trapezoid."))
                h = float(input("Please enter the h of the trapezoid."))
                print(f'The area of the trapezoid is: {Geometry.areaOfTrapezoid(a,b,h)}\n')
            else:
                print("That is not a valid option.")
            choice = input("Would you still like to calculate area?\n")
            if choice.lower() != "yes":
                break
    if choice == "2":
        while True:
            choice = input("What would you like to calculate the perimeter of?\n1 - Regular Polygon\n2 - Triangle\n3 - Rectangle\n4 - Trapezoid")
            if choice == "1":
                numOfSides = float(input("Enter in the amount of sides of the regular polygon."))
                sideLength = float(input("Enter in the length of each side."))
                print(f'The perimeter of the regular polygon is: {Geometry.perimeterRegularPolygons(numOfSides,sideLength)}\n')
            if choice == "2":
                a = float(input("Enter in the a of the triangle."))
                b = float(input("Enter in the b of the triangle."))
                c = float(input("Enter in the c of the triangle."))
                print(f'The perimeter of the triangle is: {Geometry.perimeterOfTriangle(a,b,c)}\n')
            if choice == "3":
                length = float(input("Enter the length of the rectangle."))
                width = float(input("Enter in the width of the rectangle."))
                print(f'The perimeter of the rectangle is: {Geometry.perimeterOfRectangle(length,width)}\n')
            if choice == "4":
                a = float(input("Enter the a of the trapezoid."))
                b = float(input("Enter the b of the trapezoid."))
                c = float(input("Enter in the c of the trapezoid."))
                d = float(input("Enter in the d of the trapezoid."))
                print(f"The perimeter of the trapezoid is: {Geometry.perimeterOfTrapezoid(a,b,c,d)}\n")
            else:
                print("That's not a valid option.")
            choice = input("Would you still like to calculate perimeter?")
            if choice.lower() != "yes":
                break
    if choice == "3":
        while True:
           x1 = float(input("Enter the x coordinate of the first point."))
           y1 = float(input("Enter the y coordinate of the first point."))
           x2 = float(input("Enter the x coordinate of the second point."))
           y2 = float(input("Enter the y coordinate of the second point."))
           line = Line(point1=(x1,y1),point2=(x2,y2))
           print("The coordinates you entered is: ({},{}) and ({},{})\n".format(x1,y1,x2,y2))
           choice = input("What do you want to know?\n1 - Midpoint\n2 - Slope\n3 - Length\n4 - Angle\n5 - Equation\n6 - Right Bisector Equation")
           if choice == "1":
               print("The midpoint is: {}".format(line.midpoint))
           if choice == "2":
               print("The slope is: {}".format(line.slope))
           if choice == "3":
               print("The length of the line is: √{}".format(line.length))
           if choice == "4":
               print("{}° & {}c.".format(line.angle_degrees,line.angle_radians))
           if choice == "5":
               print("The equation is: {}".format(line.equation))
           if choice == "6":
               print("The Right Bisector equation is: {}".format(line.rightBisector))

           choice = input("Would you like to do line stuff again?\n")
           if choice.lower() != "yes":
                break
    if choice == "4":
        print("Thanks for using the program. Goodbye.")
        break
