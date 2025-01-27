#Write a function that prompts the user to enter a number and tries to convert it to an
#integer. Handle the TypeError exception by printing a message indicating that the input
#is not a valid number. Use a finally block to print "Type conversion process completed."
from math import ceil,floor

def type_conversion(num):
    try:
        if 0.5 <= num - int(num):
            num = ceil(num)
            print(num)
        else:
            num = floor(num)
            print(num)
    except (ValueError,TypeError):
        print("The input is not a valid number.")
    else:
        print("Type conversion process completed.")
type_conversion(20.9)



