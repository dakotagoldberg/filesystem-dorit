
global fileSystem
global myLoc
fileSystem = "[folder:dorit[folder:winter[folder:december[folder:christmas[]][folder:kwanzaa[]]][folder:january[]][file:sleet][file:ice]]]"
myLoc = 2


def findLocation(index):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (count == index):
                return i
            count+=1

def reverseLookup(name):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (currentFolderName(count) == name):
                return count
            count+=1


def totalItems():
    return fileSystem.count(":")


def currentFolderContents(index):
    openB = 0
    closedB = 0
    for i in range(findLocation(index) + len(currentFolderName(index))+1, len(fileSystem)):
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        if openB == closedB - 1:
            return fileSystem[findLocation(index) + len(currentFolderName(index))+1:i]


def currentFolderName(index):
    i = findLocation(index)
    while (fileSystem[i] != "[" and fileSystem[i] != "]"):
        i+=1
    return fileSystem[findLocation(index)+1:i]

def itemType(index):
    i = findLocation(index)
    while (fileSystem[i] != "[" and fileSystem[i] != "]"):
        i-=1
    return fileSystem[i + 1:findLocation(index)]

def currentPath(index):
    path = []
    path.append(currentFolderName(index))
    openB = 0
    closedB = 0
    count = index
    i = findLocation(index)
    while (i > 0):
        if fileSystem[i] == ":":
            if (openB > closedB):
                path.append(str(currentFolderName(count)))
            count-=1
        if fileSystem[i] == "[":
            openB+=1
        if fileSystem[i] == "]":
            closedB +=1
        i-=1
    return path


def parseContents(index):
    raw = currentFolderContents(index)
    items = []
    openB = 0
    closedB = 0
    count = index + 1
    start = findLocation(index) + len(currentFolderName(index)) + 1
    i = start
    while (i < len(raw) + start):
        if fileSystem[i] == "[":
            openB+=1
        elif fileSystem[i] == "]":
            closedB +=1
        elif fileSystem[i] == ":":
            if (openB - closedB == 1):
                items.append(str(currentFolderName(count)))
            count+=1
        i+=1
    return items

def listContents(index):
    for i in parseContents(index):
        print(i + " --> " + itemType(reverseLookup(i)))

def changeDirectory(currentIndex, newLoc):
    if newLoc == ".." and currentIndex != 0:
        x = currentPath(currentIndex)
        return reverseLookup(x[1])
    else:
        x = parseContents(currentIndex)
        if newLoc in x and itemType(reverseLookup(newLoc)) == "folder":
            return reverseLookup(newLoc)
    return currentIndex

def createPath(input):
    input = input[1:len(input)] + "/"
    temp = ""
    numSlash = 0
    for i in range(len(input)):
        if(input[i] == '/'):
            numSlash+=1
    output = []
    numSlash = 0
    #print(output)
    for i in range(len(input)):
        if(input[i] == '/'):
            #print(temp)
            #print(output)
            output += [temp]
            temp = ""
            numSlash += 1
        else:
            temp += "" + input[i]
    return output

def touch1(input):
    tempLoc = 0
    place = createPath(input)
    for i in place:
        print(tempLoc)
        if tempLoc == None:
            print("error input not supported")
        tempLoc = changeDirectory(tempLoc, i)
    startPoint = findLocation(tempLoc)
    
    Triforce1 = fileSystem[0:startPoint + len(currentFolderName(tempLoc))+1]
    #print(Triforce1)
    Triforce2 = "[file:]"
    if(fileSystem[startPoint+ len(currentFolderName(tempLoc))+1 : startPoint+ len(currentFolderName(tempLoc))+3] == "[]"):
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+3:len(fileSystem)]
    else:
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+1:len(fileSystem)]
    #print(Triforce3)
    #print(Triforce1+Triforce2+Triforce3)
    
    return Triforce1 +Triforce2 + Triforce3
def touch2():
    tempLoc = 0
    place = currentPath(myLoc)
    for i in place:
        print(tempLoc)
        if tempLoc == None:
            print("error input not supported")
        tempLoc = changeDirectory(tempLoc, i)
    startPoint = findLocation(tempLoc)
    
    Triforce1 = fileSystem[0:startPoint + len(currentFolderName(tempLoc))+1]
    #print(Triforce1)
    Triforce2 = "[file:]"
    if(fileSystem[startPoint+ len(currentFolderName(tempLoc))+1 : startPoint+ len(currentFolderName(tempLoc))+3] == "[]"):
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+3:len(fileSystem)]
    else:
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+1:len(fileSystem)]
    #print(Triforce3)
    #print(Triforce1+Triforce2+Triforce3)
    
    return Triforce1 +Triforce2 + Triforce3
        


print(touch1(input("hey")))
