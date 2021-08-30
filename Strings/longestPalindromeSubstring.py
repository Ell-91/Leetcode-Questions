def longetsPalindromeSubstring(string):
    def expandAroundCenter(string, left_ptr, right_ptr):
        while left_ptr >= 0 and right_ptr < len(string) and string[left_ptr] == string[right_ptr]:
            left_ptr -= 1
            right_ptr += 1
        return string[left_ptr + 1:right_ptr]

    longestSub = ""

    for i in range(len(string)):
        center = expandAroundCenter(string, i, i) 
        inBetween = expandAroundCenter(string, i, i + 1)
        
        longestSub = max(longestSub, center, inBetween, key = len)

    return longestSub


string = 'abaxyzzyxf'
print(longetsPalindromeSubstring(string))