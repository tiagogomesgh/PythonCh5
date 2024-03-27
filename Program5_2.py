### Tiago Gomes - 2375703
### COP1000 -#1284
### Program5_2.py

### Pseudocode
### Within the main function, Prompt the user to enter the Length, Width, and Height of the cuboid, as floats.

### Within the calc_surface_area function, calculate the surface area and return the surfaceArea variable.
### Within the calc_diagonal function, calculate the diagonal, using the math module and return the diagonal variable.
### Within the calc_volume, calculate the volume and print the variable in a formatted f-string

import math


def main () :
    length = float(input("Enter the length of the rectangular cuboid: "))
    width = float(input("Enter the width of the rectangular cuboid: "))
    height = float(input("Enter the height of the rectangular cuboid: "))

    ### Function Calls.
    calc_surface_area(length,width,height)
    calc_diagonal(length,width,height)
    calc_volume(length,width,height)

    
def calc_surface_area (length,width,height) :
    surfaceArea = 2 * (length * width) + 2 * (length * height) + 2 * (height * width)
    print(f'The Surface Area of the rectangular cuboid is {surfaceArea:.4f}')
    return surfaceArea

def calc_diagonal (length,width,height) :
    diagonal = math.sqrt((length ** 2) + (width ** 2) + (height ** 2))
    print(f'The Diagonal of the rectangular cuboid is {diagonal:.3f}')
    return diagonal

def calc_volume (length,width,height) :
    volume = length * width * height
    print(f'The Volume of the rectangular cuboid is {volume:.3f}')

### Dunders Notation, ensures that it is being run as a standalone program, or as an imported module.
if __name__ == '__main__' :
    main()
    


   









