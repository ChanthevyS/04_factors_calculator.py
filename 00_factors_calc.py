# Functions go here
import math

def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end the statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays intructions / information
def intructions():

    statement_generator("Intructions / information", "=")
    print()
    print("Please choose a number")
    print()
    print("This program finds the factors of a number")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit. ")
    print()
    return""


# Checks input is a number more than a given value
def num_check(question, low, high):
    vaild = False 
    while not vaild:

        error = "please enter an integer that is more than {} and less than {}".format(low, high)
        
        try:

            # asks user to enter a number
            response = int(input(question))
                
            # checks number is more than zero
            if low < response < high:
                return response 

            # outputs error if input is invaild
            else: 
                print(error) 
                print()

        except ValueError:
            print(error)

    


# gets factors, returns a sorted list
def get_factors(var_to_factor):

    #Loop to allow multiple calculations per session

    comment = ""

    # ask user for number to be factored...

    factor_list = []

    # add one to square root so that when we make it an integer, our loop stops correctly
    limit = var_to_factor**(0.5) + 1
    limit = int(limit)

    for item in range(1, limit):
    
        # is it a factor....
        if var_to_factor % item == 0:
            factor_list.append(item)
            partner = var_to_factor // item

            # Only add the partner if it is not already in the list
            if partner not in factor_list:
                factor_list.append(partner)
    
    # sort the list
    factor_list.sort()


    return(factor_list)
    

# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    intructions()

#Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    to_factor = num_check("Number? ", 0, 201)
    # ask user for number to be factored...

        # output factors and comment

    # Generate heading...
    if to_factor == 1:
        heading = "One is special..."

    else:
        heading = "factors of {}".format(to_factor)

    if to_factor != 1:
        factor_list = get_factors(to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor, Itself :)"

    print(to_factor)

    # comments for squares / primes 
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
print()