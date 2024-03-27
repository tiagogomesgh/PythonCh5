### Tiago Gomes - 2375703
### COP1000 -#1284
### Program5_1.py

### Pseudocode
### PROMPT the user to enter the number of different types of shoelaces. Store as numOfStrings.
### Set the total cost to zero. 
### CREATE a For loop, iterating in a range of 1 to the numberOfStrings.
### PRINT the item # at the start of each iteration.
### PROMPT the user to enter the eyelet and quantity number.

### CREATE a subtotal module, containing a function that calculates the subtotal of the item.
### call the calc_subtotal function and store the result in a variable.
### Keep a running total, by incrementing the total variable by this subtotal.
### increment the item or counter variable.

import subtotal


def main () :
    numOfStrings = int(input("Enter the number of different types of shoelaces being purchased: "))
    
    ### sets the total cost to 0, before the start of the loop.
    total = 0
    
    ### Iterates through each item in the range, including the last integer.
    for item in range(1,numOfStrings + 1) :
        
        ### Prints the Current ITEM number
        print(f'Item {item}:')
        
        ### PROMPTS the user for each desired variable.
        orderEyelets = int(input("Enter the number of eyelet pairs: "))
        orderQuantity = int(input("Enter the quantity: "))

        ### Assigns the calculated subtotal to variable called subTotal.    
        subTotal = subtotal.calc_subtotal(orderEyelets,orderQuantity)
        ### Prints the subtotal cost, in a formatted f-string. 
        print(f'Subtotal for Item {item}: ${subTotal:.2f}\n')

        total += subTotal
        
        ### Incremenets the item or counter variable.
        item += 1
        
    ### Prints the total cost of the order after the loop has finished.   
    print(f'Total: ${total:.2f}')

### Dunders Notation, ensures that it is being run as a standalone program, or as an imported module.
if __name__ == '__main__' :
    main()


