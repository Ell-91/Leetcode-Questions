from typing import ItemsView


def validIPAddress(string):
    ipAddressesFound = []


    for i in range(1, min(len(string), 4)):
        print(len(string))
        currentIPAddress = ["","","",""]

        currentIPAddress[0] = string[:i]
        if not isValid(currentIPAddress[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            print(len(string))
            currentIPAddress[1] = string[i:j]
            if not isValid(currentIPAddress[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                print(len(string))
                currentIPAddress[2] = string[j:k]
                currentIPAddress[3] = string[k:]

                if isValid(currentIPAddress[2]) and isValid(currentIPAddress[3]):
                    ipAddressesFound.append(".".join(currentIPAddress))
    return ipAddressesFound


def isValid(string):
    stringAsInt = int(string)

    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt)) #checks for leading 0's
    

string = "1921680"
print(validIPAddress(string))