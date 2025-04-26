def taskSix():#function declaration
    digits = list(input("Enter a number to get the sum of its didgits: ")) #user inout
    sum = 0 #initialise sum to 0
    while digits: #while the listy of digits is not empty
        sum += int(digits.pop()) #loop through the list of digits, set them as integers and from the last one add them
    print (str(sum)) #display resuls
taskSix() #function call