#-------------------------------------------------------------------------------
# Name:        bubble sorting then binary search
# Purpose:
#
# Author:      Ben Jones
#
# Created:     03/02/2022
# Copyright:   (c) Ben Jones 2022
#-------------------------------------------------------------------------------

import random

randArray = []
itemFound = False

while len(randArray) < 20:
    randArray.append(random.randint(0,50))
    randArray = list(dict.fromkeys(randArray))

print("Unordered:", randArray)

numItems = 20
while numItems>1:
    for count in range(19):
        if randArray[count] > randArray[count+1]:
            temp = randArray[count]
            randArray[count] = randArray[count+1]
            randArray[count+1] = temp
            # print(randArray)
    numItems = numItems-1

print("Ordered:", randArray)

def binary_search(randArray, searchItem):  
    low = 0  
    high = len(randArray) - 1  
    mid = 0  
  
    while low <= high:    
        mid = (high + low) // 2 
        if randArray[mid] < searchItem:  
            low = mid + 1 
        elif randArray[mid] > searchItem:  
            high = mid - 1
        else:  
            return mid  
    return -1 
    
while itemFound == False:
    searchItem = int(input("Search the array: "))

    result = binary_search(randArray, searchItem)

    if result != -1:  
        print("Found at positon", str(result + 1))
        itemFound = True  
    else:  
        print("Not found, Try again")  
