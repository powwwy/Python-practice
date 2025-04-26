def taskThree(): #function declaration
    z = int(input("Let's calculate a factorial, your choice: "))#user input
    z2 = z #store the original value for later
    res = 1 #initialize result value as 1 for later
    if z == 0: #check if user input 0
        print("0! = 1")
    else: # if the value is not 0
        while z > 1: #while loop to calculate factorial
            res *= z #result = res(1) * z ad so on until the loop ends
            z -= 1 #decrement z by 1
    print(str(z2)+ "! = " + str(res)) #result
taskThree() #fucnction call