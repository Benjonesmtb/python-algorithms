from guizero import App, Text, PushButton, TextBox
import random
import time

app = App(title="Bubble Sorting and Binary Search")

randArray = []
itemFound = False

while len(randArray) < 20:
    randArray.append(random.randint(0,50))
    randArray = list(dict.fromkeys(randArray))
message1 = Text(app, text="Unordered:")
message2 = Text(app, text=randArray)

numItems = 20
while numItems>1:
    for count in range(19):
        if randArray[count] > randArray[count+1]:
            temp = randArray[count]
            randArray[count] = randArray[count+1]
            randArray[count+1] = temp
            # print(randArray)
    numItems = numItems-1

message3 = Text(app, text="Ordered:")
message4 = Text(app, text=randArray)



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
    positonFound = str(result + 1)

    if result != -1:  
        message5 = Text(app, text="Found at positon:")
        message5.value = "Found at position" + int(positonFound.value)
        itemFound = True  
    else:  
        message6 = Text(app, text="Not found, Try again")    


# button = PushButton(app, text="Press me", command=genNumbers(randArray))

app.display()