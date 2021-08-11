def longestPeak(array):
    longestPeakLength = 0 

    i = 1 
    while i < len(array) -1:
        isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]

        if not isPeak:
            i += 1
            continue

        # Expand to the left for strictly decreasig values
        leftIndex = i - 2
        while leftIndex >= 0 and array[leftIndex] < array[leftIndex + 1]:
            leftIndex -= 1

        # Expand to the right to find strickly decreasing values
        rightIndex = i + 2
        while rightIndex <= len(array) - 1 and array[rightIndex] < array[rightIndex - 1]:
            rightIndex += 1

        currentPeakLength = rightIndex - leftIndex - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIndex

    return longestPeakLength



array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))