def taskOne():#function declaration
    mySum = []  # making an empty list to allow user input
    x = int(input("Enter a range:"))  # letting the user set the amount of numbers they want
    for i in range(x):
        num = int(input("Enter Number: "))
        mySum.append(num)  # adding each new number to the list
    summy = str(sum(mySum))  # using the in built sum function to add the elements
    print("The sum of items in your list = " + summy)
    
taskOne()#function call
