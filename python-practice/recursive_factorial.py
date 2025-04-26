number = int(input("Another number for factorial: ")) # user enters the number
def taskFive(number):#function declaration, using the argument number
    if number == 0 or number == 1: #set the base case for 0 and 1
        return 1
    else: #when the number is neither 0 or 1
        return number * taskFive(number - 1) #recursive function, takes the number and multiples by the number -1 in the function
print(str(number) + "! = " + str(taskFive(number)))