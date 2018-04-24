import geometry

print("Welcome to the Ultimate Math Tool. What would you like to do?\n")
while True:
    choice = input("1 - Area\n2 - Perimeter\n3 - Lines and Stuff\n")
    if choice == "1":
        while True:
            choice = input("What would you like to calculate the area of?\n 1 - Regular Polygons\n 2 - Triangle\n 3 - Rectangle\n 4 - Trapezoid\n")
            #Reg Polygons
            if choice == "1":
                numOfSides = float(input("Enter in the amount of sides."))
                sideLength = float(input("Enter in the side length."))
                print(f'The area is: {geometry.areaRegularPolygons(numOfSides,sideLength)}\n')
            #Triangle
            if choice == "2":
                base = float(input("Enter in the base length of the triangle."))
                height = float(input("Enter in the height of the triangle."))
                print(f'The area of the triangle is: {geometry.areaOfTriangle(base,height)}\n')
            #Rectangle
            if choice == "3":
                length = float(input("Please enter the length of the rectangle."))
                width = float(input("Please enter the width."))
                print(f'The area of the rectangle is: {geometry.areaOfRectangle(length,width)}\n')
            #Trapezoid
            if choice == "4":
                a = float(input("Please enter the a of the trapezoid."))
                b = float(input("Please enter the b of the trapezoid."))
                h = float(input("Please enter the h of the trapezoid."))
                print(f'The area of the trapezoid is: {geometry.areaOfTrapezoid(a,b,h)}\n')
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
                print(f'The perimeter of the regular polygon is: {geometry.perimeterRegularPolygons(numOfSides,sideLength)}\n')
            if choice == "2":
                a = float(input("Enter in the a of the triangle."))
                b = float(input("Enter in the b of the triangle."))
                c = float(input("Enter in the c of the triangle."))
                print(f'The perimeter of the triangle is: {geometry.perimeterOfTriangle(a,b,c)}\n')
            if choice == "3":
                length = float(input("Enter the length of the rectangle."))
                width = float(input("Enter in the width of the rectangle."))
                print(f'The perimeter of the rectangle is: {geometry.perimeterOfRectangle(length,width)}\n')
            if choice == "4":
                a = float(input("Enter the a of the trapezoid."))
                b = float(input("Enter the b of the trapezoid."))
                c = float(input("Enter in the c of the trapezoid."))
                d = float(input("Enter in the d of the trapezoid."))
                print(f'The perimeter of the trapezoid is: {geometry.perimeterOfTrapezoid(a,b,c,d)}\n')
            else:
                print("That's not a valid option.")
            choice = input("Would you still like to calculate perimeter?")
            if choice.lower() != "yes":
                break








