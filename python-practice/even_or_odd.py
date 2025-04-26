def taskTwo():#function declaration
    y = int(input("Enter a number: " )) #allow user to enter number
    if y%2 == 0: #check if remainder is equal to 0
        print(str(y) + " is even.")
    else:
        print(str(y) +" is odd.")
taskTwo()#function call