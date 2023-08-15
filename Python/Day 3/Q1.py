def calculate_area(shape, value1, value2=None):
    try:
        if shape == 't':  # Triangle
            if value2 is None:
                raise ValueError("Triangle requires 2 values")
            return 0.5 * value1 * value2
    
        elif shape == 'r':  # Rectangle
            if value2 is None:
                raise ValueError("Rectangle requires 2 values")
            return value1 * value2
    
        elif shape == 's':  # Square
            if value2 is not None:
                raise ValueError("Square only requires 1 value")
            return value1 * value1
    
        elif shape == 'c':  # Circle
            if value2 is not None:
                raise ValueError("Circle only requires 1 value.")
            return 3.14159*value1*value1
    
        else:
            raise ValueError("Unsupported shape type.")
    
    except ValueError as e:
        return str(e)
shape = input("Enter shape type ").lower()

if shape in ['t', 'r']:
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))
    result = calculate_area(shape, value1, value2)
    print(f"The area is: {result}")
    
elif shape in ['s', 'c']:
    value1 = float(input("Enter the value: "))
    result = calculate_area(shape, value1)
    print(f"The area is: {result}")
    
else:
    print("Invalid shape type!")







