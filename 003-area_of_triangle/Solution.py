base = float(input("Dame la base: "))  
height = float(input("Dame la altura: "))  

def area_of_triangle(base, height):  
    area = base * height / 2  
    return area  

# Llamamos a la función con los valores introducidos y mostramos el resultado  
resultado = area_of_triangle(base, height)  
print("El área del triángulo es:", resultado)

#esto es el codigo original del ejercicio

""""# Complete the function to return the area of a triangle
def area_of_triangle(base, height):
    # Your code here, please remove the "None" 
    return base * height / 2

# Testing your function
print(area_of_triangle(3, 5))"""