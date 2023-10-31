import math

choice = input("Do you want to calculate the area of a triangle or a circle? (triangle/circle): ").lower()

if choice == "triangle":
    # Calculate the area of a triangle
    base = float(input("Enter the length of the triangle's base: "))
    height = float(input("Enter the height of the triangle: "))
    triangle_area = 0.5 * base * height
    print(f"The area of the triangle is: " + str(triangle_area))

elif choice == "circle":
    radius = float(input("Enter the radius of the circle: "))
    circle_area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {circle_area:.2f}")

else:
    print("Invalid option. Please choose 'triangle' or 'circle'.")
