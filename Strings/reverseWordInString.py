def reverseWordsInSrring(string):
    #Error checking for empty list 
    if string == []:
        return False
    
    #Create a list that stores all the words in the string
    words = []
    startIndx = 0          #keeps track of the start of our word

    for i in range(len(string)):
        character = string[i]

        if character == " ":    #First append the word
            words.append(string[startIndx:i])
            startIndx = i
        elif string[startIndx] == " ": #Then append the space 
            words.append(" ")
            startIndx = i

    words.append(string[startIndx:])

    reverseList(words)
    return "".join(words)
   
    #Helper function to reverse words in a string 
def reverseList(string):
    left_ptr = 0
    right_ptr = len(string) -1 

    while left_ptr < right_ptr:
        string[left_ptr], string[right_ptr] = string[right_ptr], string[left_ptr]
        left_ptr += 1
        right_ptr -= 1


string = "AlgoExpert is the best!"  #is the best!"  #best! the is AlgoExpert
print(reverseWordsInSrring(string))