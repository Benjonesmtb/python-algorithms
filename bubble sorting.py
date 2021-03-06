#-------------------------------------------------------------------------------
# Name:        bubble sorting
# Purpose:
#
# Author:      Ben Jones
#
# Created:     03/02/2022
# Copyright:   (c) Ben Jones 2022
#-------------------------------------------------------------------------------

import random

randArray = []

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
