def taskSix():#function declaration
    digits = list(input("Enter a number to get the sum of its digits: ")) #user input
    sum = 0 #initialise sum to 0
    while digits: #while the list of digits is not empty
        sum += int(digits.pop()) #loop through the list of digits, set them as integers and from the last one add them
    print (str(sum)) #display results
taskSix() #function call