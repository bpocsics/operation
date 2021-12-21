#Import sys.argv and operator to translate words into symbols
import sys
import operator
#Protocol is used to add or subtract based on user input
def protocol(symbol, length):
    #Declares the operators that are available
    # add for addition or sub for subtraction
    ops = {
        "add": operator.add,
        "sub": operator.sub,
    }
    #Declares num to store the output from the for loop
    num = 0.0
    #Does operator on whatever number comes after the -<num>
    for i in range(2, length):
        #num - stores the operator
        #ops[symbol] translates to + or - based on how it was called
        #modifies number in () sys.argv[i] is the position in the for loop
        num = ops[symbol](float(num),float(sys.argv[i]))
    #Prints num
    print("Your total is:", num)
#Displays help screen to user
def helpScreen():
    print("""
    Welcome to addition calculator:
    -a for addition.
    -s for subtraction.
    -h for help.
    """)
#Gets the length of how many inputs were taken in after the program was called and then calls the correct operator in the above program.
#Or, if it does not exist will notify the user
def main():
    length = len(sys.argv)

    if sys.argv[1] == '-h':
        helpScreen()
    elif sys.argv[1] == '-a':
        protocol("add", length)
    elif sys.argv[1] == '-s':
        protocol("sub", length)
    else:
        print("That does not exist, use -h for help!")


main()