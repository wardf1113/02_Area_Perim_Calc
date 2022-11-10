# functions go here

# checks input is a number more then zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"
        
        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)



# Main Routine,goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":
   
    # call your number checker function three times to get the
    # width, length and cost_per_m of the fencing
    print("Welcome to Fence Cost Calculator")
    width = num_check("Width: ")
    height = num_check("Height: ")  
    cost_per_m = num_check("cost_per_m: ")

    # Calulate perimeter (width + height) x 2
    perimeter = (width + height) * 2

    # Calulate the cost of the fencing (perimeter x price / meter)
    price = (perimeter * cost_per_m )

    # Output the perimeter and cost of the fencing
    print("Perimeter : {:.2f} m".format(perimeter))
    print("Price : ${:.2f}".format(price))
    
    keep_going = input("Press <enter> to keep going or any key to quit")
        
print()    
print("Thanks for using the Fencing cost calculator")