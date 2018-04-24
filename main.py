import lines

still_select = True


print("Welcome to the Ultimate Math Tool. What would you like to do?")
while True:
  print("Select from the following:\n1 - Area \n2 - Perimeter\n3 - Lines")
  choice = input("")
  if choice == "1":
    while still_select:
      choice = input("What shape would you like to calculate the area of?\n")
      if choice.lower() == "square":
        side = float(input("Please enter the side length of the square.\n"))
        print(f'Area of the Square is: {lines.areaOfSquare(side)}\n')
      if choice.lower() == "circle":
        radius = float(input("Please enter the radius of the circle."))
        print (f'The area of the circle is: {lines.areaOfCircle(radius)}\n')
      if choice.lower() == "triangle":
        base = float(input("Please enter the base of the triangle."))
        height = float(input("Please enter the height of the triangle."))
        print (f'The area of the triangle is: {lines.areaOfTriangle(base,height)}')
      if choice.lower() == "rectangle":
        length = float(input("Please input the length of the rectangle."))
        width = float(input("Please enter the width of the rectangle."))
        print (f'The area of the rectangle is: {lines.areaOfRectangle(length,width)}')
      else: 
       print("That is not a valid shape please try again.")
        
      
      choice = input("Would you like to calculate the area of another shape?")
      
    
  elif choice == "2":
    
  else:
    print("That is not a valid option. Please try again.\n")
  
