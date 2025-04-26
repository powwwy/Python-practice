def taskFour():#function declaration
    word = str(input("Enter a word to reverse: ")) #user input, the word they want reversed
    reverse_word = " " #initialise the reversed word
    for i in word: #create a loop becuase the task does not allow me to use in built functions or slicing
        reverse_word = i + reverse_word #add each character from the last
    print(reverse_word) 
taskFour()#function call