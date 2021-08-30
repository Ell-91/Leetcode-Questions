def ispalindrome(string):
    if string == "":
        return False

    elif len(string) == 1:
        return True
    
    else:
        right_ptr = len(string) - 1
        left_ptr = 0 

        while left_ptr <= right_ptr:
            if string[right_ptr] == string[left_ptr]:
                left_ptr += 1
                right_ptr -= 1
            else:
                return False
        return True
     




string = "a"
print(ispalindrome(string))