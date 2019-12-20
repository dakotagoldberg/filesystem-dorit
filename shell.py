global fileSystem
global myLoc
fileSystem = "[folder:dorit[folder:winter[folder:december[folder:christmas[]][folder:kwanzaa[]]][folder:january[]][file:sleet is cool][file:ice]]]"
myLoc = 0

# Returns the character index of the colon of the item at given "index" (0, 1, 2, ...)
def findLocation(index):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (count == index):
                return i
            count+=1

# Returns the "index" of the first occurance of an item of a given name in the entire system.
def reverseLookup(name):
    count = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ":":
            if (currentFolderName(count) == name):
                return count
            count+=1

# Returns the "index" of an item of a given name in the current folder.
def relativeReverseLookup(index, name):
    count = index
    for i in range(findLocation(index), len(fileSystem)):
        if fileSystem[i] == ":":
            if (currentFolderName(count) == name):
                return count
            count+=1

# Returns the total number of folders and files in the system.
def totalItems():
    return fileSystem.count(":")

# Returns a string with everything in a folder and subcontents.
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

def numberOfFilesInFolder(index):
    count = 0
    for i in parseContents(index):
        if itemType(reverseLookup(i)) == "file":
            count+=1
    return count


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


def showHelp():
    print("%5s %40s" % ("ls", "lists all items in folder")) 
    print("%5s %40s" % ("cd", "changes directory")) 
    print("%5s %40s" % ("mkdir", "creates a new directory")) 
    print("%5s %40s" % ("touch", "creates a new file")) 
    print("%5s %40s" % ("edit", "edits the contents of a file")) 
    print("%5s %40s" % ("rm", "removes a file")) 
    print("%5s %40s" % ("rmdir", "removes a folder"))  
    print("%5s %40s" % ("path", "displays path of current location"))  


def listContents(index):
    numFiles = 1
    for i in parseContents(index):
        if itemType(reverseLookup(i)) == "file":
            print(i + " --> " + itemType(reverseLookup(i)) + " ["+ str(numFiles) +"]")
            numFiles+=1
        else:
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

# Spencer does not like .split()
def createPath(input):
    input = input[1:len(input)] + "/"
    temp = ""
    numSlash = 0
    for i in range(len(input)):
        if(input[i] == '/'):
            numSlash+=1
    output = []
    numSlash = 0
    for i in range(len(input)):
        if(input[i] == '/'):
            output += [temp]
            temp = ""
            numSlash += 1
        else:
            temp += "" + input[i]
    return output


# Adds a file at the specified path.
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
    Triforce2 = "[file:null]"
    if(fileSystem[startPoint+ len(currentFolderName(tempLoc))+1 : startPoint+ len(currentFolderName(tempLoc))+3] == "[]"):
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+3:len(fileSystem)]
    else:
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+1:len(fileSystem)]

    
    return Triforce1 +Triforce2 + Triforce3


def touch2():
    tempLoc = 0
    place = currentPath(myLoc)[::-1]
    for i in place:
        print(tempLoc)
        if tempLoc == None:
            print("error input not supported")
        tempLoc = changeDirectory(tempLoc, i)
    startPoint = findLocation(tempLoc)
    
    Triforce1 = fileSystem[0:startPoint + len(currentFolderName(tempLoc))+1]
    Triforce2 = "[file:null]"
    if(fileSystem[startPoint+ len(currentFolderName(tempLoc))+1 : startPoint+ len(currentFolderName(tempLoc))+3] == "[]"):
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+3:len(fileSystem)]
    else:
        Triforce3 = fileSystem[startPoint+ len(currentFolderName(tempLoc))+1:len(fileSystem)]

    
    return Triforce1 +Triforce2 + Triforce3

def findFileGivenIn(index,fileIndex):
    raw = currentFolderContents(index)
    openB = 0
    closedB = 0
    count2 =0
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
                if(fileSystem[findLocation(count)-4:findLocation(count)]== "file"):
                    if(count2 == fileIndex):
                        print(fileSystem[findLocation(count)+1:findLocation(count)+4])
                        return(count)
                    count2+=1
                        
            count+=1
        i+=1
    return 0

def edit(fileNum):
    fileNum = fileNum - 1
    while True:
        newVal = raw_input("Enter new value: ")
        ns = ""
        for i in newVal:
            if i != " ":
                ns += i

        if not (ns.isalnum()):
            print ("Invalid value")
            return
        break

    clown = numberOfFilesInFolder(myLoc)
    place = findLocation(myLoc)

    firstString = fileSystem[:place]
    secondString = fileSystem[place:]

    temp = findLocation(findFileGivenIn(myLoc, fileNum-1))
    print (temp)
    subFind = secondString.find("]", temp)
    print(subFind)
    tempSub1 = secondString[:(temp+1)]
    print(tempSub1)
    tempSub2 = secondString[(subFind):]
    print(tempSub2)

    print("test: " + str(temp))
    return(firstString + tempSub1 + newVal + tempSub2)


def Rmdr(index, foldername):
    openB = 0
    closedB = 0
    tempLoc = changeDirectory(myLoc,foldername)
    if fileSystem[findLocation(tempLoc) + len(foldername) + 1: findLocation(tempLoc) + len(foldername) + 3] == "[]":
        return fileSystem[0: findLocation(tempLoc) - 7] + fileSystem[findLocation(tempLoc) + len(foldername) + 4: len(fileSystem)]
    else:
        print("cannot delete. Something is in that folder")


def makeDirectory(currentLoc, toName):
    if toName in parseContents(currentLoc):
        print("A folder with that name already exists.")
        return fileSystem
    else:
        newName = toName
    currentFolderLength = len(currentFolderContents(currentLoc))
    toInsertIndex = findLocation(currentLoc) + currentFolderLength + len(itemType(currentLoc))
    newSystem = fileSystem[:toInsertIndex + 1] + "[folder: " + newName + "[]]" + fileSystem[toInsertIndex:]
    print(fileSystem[toInsertIndex:])
    print(currentFolderLength)
    print(newSystem)
    return fileSystem


while (True):
    command = raw_input(currentFolderName(myLoc) + ": ")
    # The big IF: based on command entered, run specific action.
    inputs = command.split(" ")
    if (inputs[0] == "help"):
        showHelp()
    elif (inputs[0] == "path"):
        currentPath(myLoc)
    elif (inputs[0] == "ls"):
        listContents(myLoc)
    elif (inputs[0] == "cd"):
        myLoc = changeDirectory(myLoc, inputs[1])
    elif (inputs[0] == "edit"):
        tempLoc = currentFolderName(myLoc)
        if (int(inputs[1]) == 0 or int(inputs[1]) > numberOfFilesInFolder(myLoc)):
            print("Not a valid file")
        else:
            fileSystem = edit(int(inputs[1]))
        myLoc = reverseLookup(tempLoc)
        print(fileSystem)
    elif (inputs[0] == "mkdir"):
        fileSystem = makeDirectory(myLoc, inputs[1])
    elif (inputs[0] == "touch" and len(inputs) == 1):
        fileSystem = touch2()
    elif (inputs[0] == "touch"):
        tempLoc = currentFolderName(myLoc)
        fileSystem = touch1(inputs[1])
        myLoc = reverseLookup(tempLoc)
    elif (inputs[0] == "rmdir"):
        fileSystem = Rmdr(myLoc,""+inputs[1])


makeDirectory(0)