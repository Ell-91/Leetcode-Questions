def spiralTraverse(array):
    result = []

   #variables to keep track of the rows and the colums
    start_row = 0
    end_row = len(array) -1 
    
    start_col = 0
    end_col = len(array[0]) - 1  # length of inner array (initialized to 3)

    while start_row <= end_row and start_col <= end_col:

        # Get first row of 2D array
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        # Get last column of 2D array
        for row in range(start_row + 1, end_row + 1):
            result.append([row][end_col])

        # Get last row of 2D array
        '''for col in range(end_col - 1, start_col + 1):
            result.append(array[end_row][col])
        
        for row in range(end_row - 1, start_row + 1): 
            result.append(array[row][start_col]) '''

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        
        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            result.append(array[row][start_col]) 
        
        start_row += 1
        end_row -= 1

        start_col += 1
        end_col -= 1

    return result



array =[[1,2,3,5], [12, 13, 14,5], [11, 16, 15, 6], [10, 9, 8,7]]
print(spiralTraverse(array))