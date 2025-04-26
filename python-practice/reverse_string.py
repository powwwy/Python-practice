subject = str(input("Enter something to reverse: ")) #user input
letters = len(subject) - 1 #getting the indexes of the letters in the string
def taskFour(subject, letters): #function with parameters
    if letters < 0: #base case
        return ""
    else:
        return subject[letters] + taskFour(subject, letters - 1) #using a recursive function to return the string from the last character
print(taskFour(subject, letters))#output result
    
    