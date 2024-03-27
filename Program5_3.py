### Tiago Gomes - 2375703
### COP1000 -#1284
### Program5_3.py

### Pseudocode
### Create a main function prompting the user to enter length, width and height, similar to 5_2.
### import Program5_2 as a module.
### call the needed functions as needed.
### Ensure that Program5_2, contains the necessary dunders-notation if statement, to determine if it is being run as a module
### or as a Standalone program.

import Program5_2


def main () :

    length = float(input("Enter the length of the rectangular cuboid: "))
    width = float(input("Enter the width of the rectangular cuboid: "))
    height = float(input("Enter the height of the rectangular cuboid: "))

    Program5_2.calc_surface_area(length,width,height)
    Program5_2.calc_diagonal(length,width,height)
    Program5_2.calc_volume(length,width,height)

### Dunders Notation, ensures that it is being run as a standalone program, or as an imported module.
if __name__ == '__main__' :
    main()



